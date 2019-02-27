# MQTT Client demo Continuously monitor two different MQTT topics for data, check if the
# received data matches two predefined 'commands'

import paho.mqtt.client as mqtt
from Rover import Rover

host_address='test.mosquitto.org'
speed=1, step=1, sp0 =0.15, agX = 90, agY = 180
rover = Rover(speed,step,sp0,agX,agY)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    # Subscribing in on_connect() - if we lose the connection and reconnect then
    # subscriptions will be renewed.
    client.subscribe('atnmsRover/CMcontrol')
    client.subscribe('atnmsRover/MMcontrol')

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg.payload=msg.payload.decode('utf-8')
    print(str(msg.payload))

    if msg.payload =='mmFW':
        rover.mmFW()
        
    elif msg.payload=='mmFWL':
        rover.mmFWL()
    
    elif msg.payload=='mmFWR':
        rover.mmFWR()
        
    elif msg.payload=='mmBW':
        rover.mmBW()



# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host_address, 1883, 60)

# Process network traffic and dispatch callbacks. This will also handle reconnecting.
# Check the documentation at https://github.com/eclipse/paho.mqtt.python for information
# on how to use other loop*() functions
client.loop_forever()
