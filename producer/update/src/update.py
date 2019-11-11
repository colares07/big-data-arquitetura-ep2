import json
from connection_queue import ConnectionQueue
from user_event import UserEvent
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/api/v1/user/<int:userId>', methods=['PUT'])
def put_user(userId):
    queue = ConnectionQueue(exchange='ep2', host='queue')
    content = request.get_json()
    content['id'] = userId
    metadata = UserEvent.create(content, event='update')
    message=json.dumps(metadata)
    queue.send(message=message)
    return Response(message, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
