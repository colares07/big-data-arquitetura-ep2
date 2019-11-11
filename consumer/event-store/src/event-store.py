import json
from datetime import datetime
from connection_queue import ConnectionQueue
from database_mongo import DatabaseMongo

DATABASE = "EP2"
COLLECTION = "event-store"

db = DatabaseMongo(database=DATABASE, host="database")

def callback(ch, method, properties, body):
    msg = json.loads(body)
    msg['datetime'] = datetime.now()
    
    db.add(collection=COLLECTION, json=msg)

queue = ConnectionQueue(exchange='ep2', host='queue')
queue.consume(callback=callback)

