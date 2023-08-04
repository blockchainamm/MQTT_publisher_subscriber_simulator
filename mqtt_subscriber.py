import paho.mqtt.client as paho
from paho import mqtt
import time
import os
from dotenv import load_dotenv # pip install python-dotenv. This takes environment variables from .env

# Load User name, password, and API key from the environment variables
load_dotenv()
user_name = os.environ.get('USER')
password = os.environ.get('PASSWORD')
HIVE_KEY = os.getenv("HIVE_KEY")

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# print message, useful for checking if it was successful
def on_message(client, userdata, message):
    print(f'Received message: {str(message.payload.decode("utf-8"))}')

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="Smartphone", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(user_name, password)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HIVE_KEY, 8883)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_subscribe = on_subscribe
client.on_message = on_message
time.sleep(60)
client.loop_stop()