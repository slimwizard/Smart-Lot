#!python
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from random import sample
from sqlalchemy.dialects.postgresql import UUID
from models import *

POSTGRES = {
    'user': 'smartlot_db_admin',
    'pw': 'smarterparking1',
    'db': 'smartlot_db_public2',
    'host': 'smartlot-db-public2.cxzkctjwsfey.us-east-1.rds.amazonaws.com',
    'port': '5432',
}

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)

FLAG = 0


@app.route('/')
def index():
    return "Hewwo wowwd"


@app.route('/smart-lot/lots/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file"
    file = request.files['file']
    file.save("static/test.jpg")
    return "Saved successfully"


@app.route('/smart-lot/lots', methods=['GET'])
def get_tasks():
    return jsonify({'lots': lots})


@app.route('/smart-lot/lots/<string:lot_name>', methods=['GET'])
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

# flag should be 0 or 1
# 1 being true, 0 being false


@app.route('/smart-lot/test/<int:api_flag>', methods=['GET'])
def flag_bit(api_flag):
    global FLAG
    FLAG = api_flag
    return simulate_activity()


def simulate_activity():
    global FLAG
    spots = db.session.query(NethkenA).all()
    for i in sample(range(1, len(spots)), 3):
        temp_spot = db.session.query(
            NethkenA).filter_by(spot_number=i).first()
        if temp_spot.spot_number == i and temp_spot.occupied == True:
            row_changed = db.session.query(NethkenA).filter_by(
                spot_number=i).update(dict(occupied=True))
            db.session.commit()
        elif temp_spot.spot_number == i and temp_spot.occupied == False:
            row_changed = db.session.query(NethkenA).filter_by(
                spot_number=i).update(dict(occupied=False))
            db.session.commit()
    return ''.join(['spot: {}\noccupied:{}\n'.format(
        i.spot_number, i.occupied) for i in spots])


@app.errorhandler(404)
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
    app.run(debug=True)
