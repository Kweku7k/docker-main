import pika, json
import os

from products.models import Product

import django
django.setup()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')  # Replace with your project’s settings path

connection = pika.BlockingConnection(pika.URLParameters(
    'amqps://zjdsjlug:RB7o2wtG3rRfPzuE4jhCk49jsSKnczmY@moose.rmq.cloudamqp.com/zjdsjlug?heartbeat=600'))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    product('Product likes increased')


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# channel.close()
