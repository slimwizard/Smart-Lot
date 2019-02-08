#!python
from flask import Flask, jsonify, make_response, request, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from models import NethkenA

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

lots = [
    {
        'id': 1,
        'title': u'asdf',
        'description': u'asdf'
    },
    {
        'id': 2,
        'title': u'asdf',
        'description': u'asdf'
    }
]


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


@app.route('/smart-lot/lots/<int:lot_id>', methods=['GET'])
def get_lot(lot_id):
    lot = [lot for lot in lots if lot['id'] == lot_id]
    if len(lot) == 0:
        abort(404)
    return jsonify({'lot': lot[0]})

# flag should be 0 or 1
# 1 being true, 0 being false


@app.route('/smart-lot/test/<int:flag>', methods=['GET'])
def simulate_activity(flag):
    spots = db.session.query(NethkenA).all()
    print(''.join(['spot: {}\noccupied:{}\n'.format(
        i.spot_number, i.occupied) for i in spots]))
    return 'testy'


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
