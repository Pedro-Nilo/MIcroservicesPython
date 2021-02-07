import json
import pika

params = pika.URLParameters(
    'amqps://jeeksves:HhXTU70Fw0R5EpujJFZokHw72tyxZcrG@barnacle.rmq' +
    '.cloudamqp.com/jeeksves')

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
