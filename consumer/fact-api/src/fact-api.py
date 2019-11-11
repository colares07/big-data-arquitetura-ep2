import json, redis
from flask import Flask, request, Response

app = Flask(__name__)

db = redis.Redis(host='database')

@app.route('/api/v1/fact', methods=['GET'])
def get_accountant():
    response = []
    for k in db.keys():
        kLoads = json.loads(k)
        response.append(json.loads(db.get(kLoads)))

    response = json.dumps(response)
    return Response( response, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
