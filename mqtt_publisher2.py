import paho.mqtt.client as paho
from paho import mqtt
from random import randrange, uniform
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

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="Outside_Temperature", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(user_name, password)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HIVE_KEY, 8883)

# setting callbacks, use separate functions like above for better visibility
# client.on_subscribe = on_subscribe
# client.on_message = on_message


while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    client.on_publish = on_publish
    print(f'Published {str(randNumber)} to topic TEMPERATURE')
    time.sleep(2)