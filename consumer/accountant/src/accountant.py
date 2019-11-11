import json, redis
from user_event import UserEvent
from record import Record
from connection_queue import ConnectionQueue

FIELD_CREATE = 'user_create'
FIELD_UPDATE = 'user_update'
FIELD_DELETE = 'user_delete'

db = redis.Redis(host='database')

def callback(ch, method, properties, body):
    msg = json.loads(body)
    event = UserEvent.get_event(msg)

    db.set(FIELD_CREATE, Record.count(db=db, event=event, compareEvent='create', field=FIELD_CREATE))
    db.set(FIELD_UPDATE, Record.count(db=db, event=event, compareEvent='update', field=FIELD_UPDATE))
    db.set(FIELD_DELETE, Record.count(db=db, event=event, compareEvent='delete', field=FIELD_DELETE))

queue = ConnectionQueue(exchange='ep2', host='queue')
queue.consume(callback=callback)
