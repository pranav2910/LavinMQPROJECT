import pika, os
from dotenv import load_dotenv

load_dotenv()

# Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL','amqps://foubdvbf:hVXTqzb_X6CYFaSb8iwjy4jZgnOY_R3o@duck.lmq.cloudamqp.com/foubdvbf')

# Create a connection
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
print("[✅] Connection over a channel created")

# start a channel
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello_world')


def send_to_queue(channel, routing_key, body):
    channel.basic_publish(
        exchange='',
        routing_key=routing_key,
        body=body
    )
    print(f"[📥] Message sent to queue - msg:  #{body}")


# Publish message
send_to_queue(
    channel=channel, routing_key="hello_world", body="Hello World"
)
send_to_queue(
    channel=channel, routing_key="hello_world", body="Hello World"
)
send_to_queue(
    channel=channel, routing_key="hello_world", body="Hello World"
)
try:
    connection.close()
    print("[❎] Connection closed")
except Exception as e:
    print(f"Error:cd  #{e}")