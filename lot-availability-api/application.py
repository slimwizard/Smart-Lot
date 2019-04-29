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
import time
from extract_and_predict import extract_and_predict


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
application.config['LOT_INFO'] = {}

db = SQLAlchemy(application)

# index endpoint for smoke testing
@application.route('/')
def index():
    return "Hewwo wowwd"

# gets all spots in a lot by lot id
@application.route('/smart-lot/lots/<id>', methods=['GET'])
def get_lot(id):
    application.config['LOT_INFO'] = db.session.query(Spots).filter_by(lot_id=id).all()
    rows = []
    for row in application.config['LOT_INFO']:
        rows.append(row.as_dict())
    if len(rows) == 0:
        abort(404)
    response = jsonify(rows)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

# gets all lot info by id
@application.route('/smart-lot/lots/lot/<id>', methods=['GET'])
def get_lot_info(id):
    lot_info = db.session.query(Lots).filter_by(lot_id=id)
    rows = []
    for row in lot_info:
        rows.append(row.as_dict())
    if len(rows) == 0:
        abort(404)
    response = jsonify(rows)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

# does something w profiler maybe?
@application.route('/smart-lot/lots/polling/<id>', methods=['GET'])
def get_lot_polling(id):
    while True:
        updated_lot = db.session.query(Spots).filter_by(lot_id=id).all()
        updated_rows = []
        rows = []
        for row in updated_lot:
            updated_rows.append(row.as_dict())
        for row in application.config['LOT_INFO']:
            rows.append(row.as_dict())
        if len(rows) == 0 or len(updated_rows) == 0:
            abort(404)
        if rows != updated_rows:
            response = jsonify(updated_rows)
            application.config['LOT_INFO'] = updated_lot
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
        time.sleep(5)

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

def update_db_upon_rec(spot_num, lot_id, occ):
    row_changed = db.session.query(Spots).filter_by(spot_number=spot_num,
            lot_id=lot_id).update(dict(occupied=occ))
    db.session.commit()
    print('Spot {} occupied updated to {}.'.format(spot_num, occ))

@application.route('/api/upload/<string:lot_id>/<string:key>', methods=['POST'])
def receive_image(lot_id, key):
    if key == "shoop":
        if 'file' not in request.files:
            return "ERROR: File upload failed. No file in payload."
        file = request.files['file']

        if file.filename == '':
            return "ERROR: File upload failed. File has no filename."
        
        if file and allowed_file(file.filename):
            results = extract_and_predict(file)
            for i in range(0, len(results)):
                if results[i]['status'] == "occupied":
                    update_db_upon_rec(i+1, lot_id, True)
                else:
                    update_db_upon_rec(i+1, lot_id, False)
            return jsonify(results), 200
    else:
        return "ERROR: Invalid key.", 405

# flag should be 0 or 1
# 1 being true, 0 being false

@application.route('/smart-lot/test/<string:lot_id>/<int:api_flag>', methods=['GET'])
def flag_bit(lot_id, api_flag):
    updated_spots = simulate_activity(lot_id, 1)
    return ''.join(['spot:{}\noccupied:{}\n'.format(
        i.spot_number, i.occupied) for i in updated_spots])

def simulate_activity(lot, flag):
    if flag:
        spots = db.session.query(Spots).filter_by(lot_id=lot).all()
        for i in sample(range(1, len(spots)), 3):
            temp_spot = db.session.query(Spots).filter_by(spot_number=i).first()
            if temp_spot.spot_number == i and temp_spot.occupied == True:
                row_changed = db.session.query(Spots).filter_by(spot_number=i).update(dict(occupied=False))
                db.session.commit()
            elif temp_spot.spot_number == i and temp_spot.occupied == False:
                row_changed = db.session.query(Spots).filter_by(spot_number=i).update(dict(occupied=True))
                db.session.commit()
        return spots
    else:
        return "stopped"

@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
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
