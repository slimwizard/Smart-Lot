#!python
from flask import Flask, jsonify, make_response, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from random import sample
from sqlalchemy.dialects.postgresql import UUID
from models import *
import geopy.distance
from PIL import Image, ImageEnhance
import os
import subprocess
from pathlib import Path
import numpy as np

UPLOAD_FOLDER = Path("../images/")

ALLOWED_EXTENSIONS = set(['png', 'jpg'])

POSTGRES = {
    'user': os.environ['DB_USER'],
    'pw': os.environ['DB_PW'],
    'db': os.environ['DB_NAME'],
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
}

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
application.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)

db = SQLAlchemy(application)


@application.route('/')
def index():
    return "Hewwo wowwd"


@application.route('/smart-lot/lots/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file"
    file = request.files['file']
    file.save("static/test.jpg")
    return "Saved successfully"


@application.route('/smart-lot/lots', methods=['GET'])
def get_tasks():
    return jsonify({'lots': lots})


@application.route('/smart-lot/lots/<string:lot_name>', methods=['GET'])
def get_lot(lot_name):
    print(lot_name)
    lot_info = db.session.query(eval(lot_name)).all()
    rows = []
    for row in lot_info:
        rows.append(row.as_dict())
    if len(lot_info) == 0:
        abort(404)
    response = jsonify(rows)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route('/smart-lot/lots/by_location/<string:lat_long>', methods=['GET'])
def get_lots_by_location(lat_long):
    print(lat_long)
    location_list = lat_long.split(",")
    my_coords = (location_list[0], location_list[1])
    lots = []
    lot_info = db.session.query(eval("Lots")).all()
    for row in lot_info:
        lot_coords = (row.latitude, row.longitude)
        if geopy.distance.distance(my_coords, lot_coords).mi < 20:
            lots.append(row.as_dict())

    if len(lot_info) == 0:
        abort(404)
    response = jsonify(lots)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route('/smart-lot/upload/<string:lot_id>/<string:key>', methods=['POST'])
def receive_image(lot_id, key):
    if key == "shoop":
        if 'file' not in request.files:
            return "ERROR: File upload failed. No file in payload."
        file = request.files['file']

        if file.filename == '':
            return "ERROR: File upload failed. File has no filename."

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                application.config['UPLOAD_FOLDER'], filename))
            img = Image.open(UPLOAD_FOLDER / filename)
            img = img.rotate(5)
            img.save(UPLOAD_FOLDER / filename)

            row = {}
            spot_id = 0
            row1_spot_len = 85
            for i in range(320, 700, row1_spot_len):
                spot_id += 1
                row[spot_id] = img.crop((i, 440, i+row1_spot_len, 540))
            for i in row:
                cont = ImageEnhance.Contrast(row[i]).enhance(3.0)
                bright = ImageEnhance.Brightness(cont).enhance(1.0)
                sharp = ImageEnhance.Sharpness(bright).enhance(2.5)
                sharp.save('../image-processing-server/tmp', format='PNG')
                proc = subprocess.Popen(('python3',
                                         '../image-processing-server/detection.py',
                                         'tmp'), stdout=subprocess.PIPE)
                output = proc.communicate()[0]
                if output.decode('utf-8').strip() == 'SUCCESS':
                    row_changed = db.session.query(Spots).filter_by(
                        spot_number=i).update(dict(availability=False))
                    db.session.commit()
                    print('Spot {} availability updated to {}'.format(i, True))
                else:
                    row_changed = db.session.query(Spots).filter_by(
                        spot_number=i).update(dict(availability=True))
                    db.session.commit()
                    print('Spot {} availability updated to {}'.format(i, True))
            return "File uploaded successfully", 200
    else:
        return "ERROR: Invalid key.", 405


def get_all_rows(table_name):
    rows = db.session.query(table_name).all()
    return rows

# flag should be 0 or 1
# 1 being true, 0 being false


@application.route('/smart-lot/test/flag_bit/<lot_id>/<api_flag>', methods=['GET'])
def flag_bit(lot_id=None, api_flag=None):
    updated_spots = simulate_activity('lot_id', 1)
    return ''.join(['spot:{}\navailability:{}\n'.format(
        i.spot_number, i.availability) for i in updated_spots])


def simulate_activity(lot, flag):
    if flag:
        spots = db.session.query(Spots).all()
        for i in sample(range(1, len(spots)), 3):
            temp_spot = db.session.query(
                Spots).filter_by(spot_number=i).first()
            if temp_spot.spot_number == i and temp_spot.availability == True:
                row_changed = db.session.query(Spots).filter_by(
                    spot_number=i).update(dict(availability=False))
                db.session.commit()
            elif temp_spot.spot_number == i and temp_spot.availability == False:
                row_changed = db.session.query(Spots).filter_by(
                    spot_number=i).update(dict(availability=True))
                db.session.commit()
        return spots
    else:
        return "stopped"


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

### POST for JSON data if we need it down the road ###
# @app.route('/smatr-lot/lots', methods=['POST'])
# def create_task():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     lot = {
#         'id': tasks[-1]['id'] + 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(lot)
#     return jsonify({'lot': lot}), 201


if __name__ == '__main__':
    application.run()
