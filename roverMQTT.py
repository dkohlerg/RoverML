# MQTT Client demo Continuously monitor two different MQTT topics for data, check if the
# received data matches two predefined 'commands'

import paho.mqtt.client as mqtt
from Rover import Rover
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

host_address='broker.hivemq.com'
speed=1
step=0.1
sp0 =0.15
agX = 90
agY = 180
rover = Rover(speed,step,sp0,agX,agY,kit)
global actualmsg
actualmsg = None


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
    global actualmsg
    actualmsg=msg.payload
    print('payload= ' + str(msg.payload))

    '''
    if actualmsg == 'cmL':
            rover.cmL()

    elif actualmsg == 'cmR':
            rover.cmR()

    elif actualmsg == 'cmUP':
            rover.cmUP()

    elif actualmsg == 'cmDW':
            rover.cmDW()
    '''
        
    if actualmsg =='mmFW':
        rover.mmFW()
        
    elif actualmsg=='mmFWL':
        rover.mmFWL()
    
    elif actualmsg=='mmFWR':
        rover.mmFWR()
        
    elif actualmsg=='mmBW':
        rover.mmBW()

    elif actualmsg=='StpFWLR':
        rover.stp()

    elif actualmsg=='StpFWBW':
        rover.stp()
        

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host_address, 1883, 60)

# Process network traffic and dispatch callbacks. This will also handle reconnecting.
# Check the documentation at https://github.com/eclipse/paho.mqtt.python for information
# on how to use other loop*() functions


while True:
    
    client.loop_start()

    while actualmsg == 'cmL':
            rover.cmL()

    while actualmsg == 'cmR':
            rover.cmR()

    while actualmsg == 'cmUP':
            rover.cmUP()

    while actualmsg == 'cmDW':
            rover.cmDW()

