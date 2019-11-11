import json
from connection_queue import ConnectionQueue
from user_event import UserEvent
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/api/v1/user', methods=['POST'])
def post_user():
    queue = ConnectionQueue(exchange='ep2', host='queue')
    content = request.get_json()
    metadata = UserEvent.create(content, event='create')
    message=json.dumps(metadata)
    queue.send(message=message)
    return Response(message, status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
