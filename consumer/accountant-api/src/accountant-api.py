import json, redis
from flask import Flask, request, Response

app = Flask(__name__)

FIELD_CREATE = 'user_create'
FIELD_UPDATE = 'user_update'
FIELD_DELETE = 'user_delete'

db = redis.Redis(host='database')

def get_value(db, field):
    if db.exists(field):
        return int(db.get(field))
    return 0

@app.route('/api/v1/accountant', methods=['GET'])
def get_accountant():
    response = {} 
    response[FIELD_CREATE] = get_value(db, FIELD_CREATE)   
    response[FIELD_UPDATE] = get_value(db, FIELD_UPDATE)   
    response[FIELD_DELETE] = get_value(db, FIELD_DELETE)    

    response = json.dumps(response)

    return Response( response, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
