import json
from flask import Flask, request, Response
from database_mongo import DatabaseMongo
from bson import Binary, Code
from bson.json_util import dumps

DATABASE = "EP2"
COLLECTION = "event-store"

app = Flask(__name__)

db = DatabaseMongo(database=DATABASE, host="database")

@app.route('/api/v1/event-store', methods=['GET'])
def get():
    response = db.get(collection=COLLECTION)
    response = dumps(response)
    return Response( response, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
