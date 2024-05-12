import pika, os, sys
from dotenv import load_dotenv

load_dotenv()
# Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL','amqps://foubdvbf:hVXTqzb_X6CYFaSb8iwjy4jZgnOY_R3o@duck.lmq.cloudamqp.com/foubdvbf')

# Create a connection
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
print("[✅] connection over a channel established")

# start a channel
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello_world')

def callback(ch, method, properties, body):
    print(f"[✅] Received #{ body }")

channel.basic_consume(
    "hello_world",
    callback,
    auto_ack=True,
)

try:
    print("\n[❎] Waiting for messages. To exit press CTRL+C \n")
    channel.start_consuming()
except Exception as e:
    print(f"Error: #{e}")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

