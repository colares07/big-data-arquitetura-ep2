import json, redis
from user_event import UserEvent
from connection_queue import ConnectionQueue

db = redis.Redis(host='database')

def callback(ch, method, properties, body):
    msg = json.loads(body)
    id = UserEvent.get_id(msg)
    event = UserEvent.get_event(msg)

    if event == 'create' or event == 'update':
        db.set(id, json.dumps(UserEvent.get(msg)))
    else:
        db.delete(id)

queue = ConnectionQueue(exchange='ep2', host='queue')
queue.consume(callback=callback)