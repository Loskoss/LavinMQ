import pika
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

# Create a connection
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
print("[✅] Connection over channel established")

# Start a channel
channel = connection.channel()

# Define user groups
user_groups = ["engineering", "sales", "finance"]

# Get user group argument from command line
try:
    user_group = sys.argv[1]
except IndexError:
    sys.stderr.write("Usage: %s [engineering] [sales] [finance]\n" % sys.argv[0])
    sys.exit(1)

# Check if user group is valid
if user_group not in user_groups:
    sys.stderr.write("Invalid argument - allowed arguments: %s [engineering] [sales] [finance]\n" % sys.argv[0])
    sys.exit(1)

# Define queue name, binding key, and exchange name based on user group
queue_name = f"{user_group}_queue"
queue_binding_key = user_group
exchange_name = "slack_notifications_fanout"

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type='direct'
)

# Declare queue
channel.queue_declare(
    queue=queue_name,
    durable=True
)

# Create a binding
channel.queue_bind(
    exchange=exchange_name,
    queue=queue_name,
    routing_key=queue_binding_key
)

# Define callback function
def callback(ch, method, properties, body):
    print(f"[✅] Received #{body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming messages
try:
    print("\n[❎] Waiting for messages. To exit, press CTRL+C\n")
    channel.basic_consume(queue_name, callback)
    channel.start_consuming()
except KeyboardInterrupt:
    print("\n[✅] Exiting...")
    connection.close()
except Exception as e:
    print(f"Error: {e}")
    connection.close()
