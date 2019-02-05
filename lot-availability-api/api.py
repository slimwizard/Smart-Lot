#!python
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

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

@app.route('/smart-lot/lots', methods=['GET'])
def get_tasks():
    return jsonify({'lots': lots})

@app.route('/smart-lot/lots/<int:lot_id>', methods=['GET'])
def get_lot(lot_id):
    lot = [lot for lot in lots if lot['id'] == lot_id]
    if len(lot) == 0:
        abort(404)
    return jsonify({'lot': lot[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/smatr-lot/lots', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    lot = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(lot)
    return jsonify({'lot': lot}), 201

if __name__ == '__main__':
    app.run(debug=True)