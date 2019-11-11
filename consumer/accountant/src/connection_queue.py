import pika, requests, time

class ConnectionQueue:
    def _createConnection(self, wait=0.5):
        try: 
           opt = requests.options(self._url)
        except:
           time.sleep(wait)
           self._createConnection(wait=(wait+0.5)) 

        return pika.BlockingConnection(pika.ConnectionParameters(host=self._host))
   

    def __init__(self, exchange='exchange', host='localhost'):
        self._host = host
        self._url = 'http://'+self._host+':15672'
        self._exchange = exchange
        self._connection = self._createConnection()
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type='fanout')

    def send(self, message):
        self._channel.basic_publish(exchange=self._exchange, routing_key='', body=message)

    def close(self):
        self._connection.close()

    def consume(self, callback, queue=''):
        self._result = self._channel.queue_declare(queue=queue, exclusive=True)
        self._queue_name = self._result.method.queue
        self._channel.queue_bind(exchange=self._exchange, queue=self._queue_name)
        self._channel.basic_consume(queue=self._queue_name, on_message_callback=callback, auto_ack=True)
        self._channel.start_consuming()
        print('consume ON')




