import django
import json
import os
import pika


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters(
    'amqps://jeeksves:HhXTU70Fw0R5EpujJFZokHw72tyxZcrG@barnacle.rmq' +
    '.cloudamqp.com/jeeksves')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def subscribe(channel, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)

    if properties.content_type == 'product_liked':
        product = Product.objects.get(id=id)

        product.likes = product.likes + 1
        product.save()

        print('Product likes increased')


channel.basic_consume(queue='admin', on_message_callback=subscribe,
                      auto_ack=True)

print('Start consuming')

channel.start_consuming()

channel.close()
