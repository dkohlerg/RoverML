from evdev import InputDevice, ecodes
import paho.mqtt.publish as publish

evnum = input('Introduzca el numero de evento del mando: ')
gamepad=InputDevice('/dev/input/event'+str(evnum))

print(gamepad)

# Codigo de botones

btn1=304
btn2=305
btn3=307
btn4=308

btnSelect=314
btnStart=315
btnPlay=319

btnL=310
btnR=311
btnY=17
btnX=16

# host name MQTT

host_address='test.mosquitto.org'

for event in gamepad.read_loop():
    
    # Digitales
    
    if event.type == ecodes.EV_KEY:

        if event.code == btn1:
            if event.value == 1:
                publish.single('atnmsRover/CMcontrol','CMDW',hostname=host_address)
                print('CMDW published')
            elif event.value == 0:
                publish.single('atnmsRover/CMcontrol','StpCMDW',hostname=host_address)
                print('StpCMDW published')

#        elif event.code == btn2:
#            if event.value == 1:
#                print('Pulsado btn2')
#            elif event.value == 0:
#                print('btn2 released')
                
        elif event.code == btn3:
            if event.value == 1:
                publish.single('atnmsRover/CMcontrol','CMUP',hostname=host_address)
                print('CMUP published')
            elif event.value == 0:
                publish.single('atnmsRover/CMcontrol','StpCMUP',hostname=host_address)
                print('StpCMUP published')

#        elif event.code == btn4:
#            if event.value == 1:
#                print('Pulsado btn4')
#            elif event.value == 0:
#                print('btn4 released')

        elif event.code == btnR:
            if event.value == 1:
                publish.single('atnmsRover/CMcontrol','CMR',hostname=host_address)
                print('CMR published')
            elif event.value == 0:
                publish.single('atnmsRover/CMcontrol','StpCMR',hostname=host_address)
                print('StpCMR published')
                
        elif event.code == btnL:
            if event.value == 1:
                publish.single('atnmsRover/CMcontrol','CML',hostname=host_address)
                print('CML published')
            elif event.value == 0:
                publish.single('atnmsRover/CMcontrol','StpCML',hostname=host_address)
                print('StpCML published')
                
        elif event.code == btnStart:
            if event.value == 1:
                publish.single('atnmsRover/CMcontrol','START',hostname=host_address)
                print('START published')
                
#        elif event.code == btnSelect:
#            if event.value == 1:
#                print('Pulsado btnSelect')
#            elif event.value == 0:
#                print('btnSelect released')
#                
#        elif event.code == btnStart:
#            if event.value == 1:
#                print('Pulsado btnStart')
#            elif event.value == 0:
#                print('btnStart released')

    # Analog
    
    else:
        if event.code == btnY:
            if event.value == -1:
                publish.single('atnmsRover/MMcontrol','MMFW',hostname=host_address)
                print('MMFW published')
            elif event.value == 1:
                publish.single('atnmsRover/MMcontrol','MMBW',hostname=host_address)
                print('MMBW published')
            else:
                publish.single('atnmsRover/MMcontrol','StpFWBW',hostname=host_address)
                print('StpFWBW published')
                
        elif event.code == btnX:
            if event.value == -1:
                publish.single('atnmsRover/MMcontrol','MMFWL',hostname=host_address)
                print('MMFWL published')
            elif event.value == 1:
                publish.single('atnmsRover/MMcontrol','MMFWR',hostname=host_address)
                print('MMBWR published')
            else:
                publish.single('atnmsRover/MMcontrol','StpFWLR',hostname=host_address)
                print('StpFWLR published')

