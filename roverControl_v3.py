from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
from evdev import InputDevice, categorize, ecodes
gamepad=InputDevice('/dev/input/event0')
print(gamepad)
kit = ServoKit(channels=16)

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


# Variables auxiliares

speed=1
step=1
sp0 =0.15

anguloX = 90
anguloY = 180

def brazo(a):
    if a < 0:
        return 0
    elif a > 180:
        return 180
    else:
        return a
    
def rueda(a):
        if a>0:
                return 1
        else:
                return 0
        
def forward(a):
    kit.continuous_servo[13].throttle = -a*speed
    kit.continuous_servo[12].throttle = a*speed
    
def rotateL():
    kit.continuous_servo[13].throttle = speed
    kit.continuous_servo[12].throttle = sp0
    
def rotateR():
    kit.continuous_servo[13].throttle = sp0
    kit.continuous_servo[12].throttle = -speed
           
def brake():
    kit.continuous_servo[13].throttle = sp0
    kit.continuous_servo[12].throttle = sp0
    

def camX(value):
    global anguloX
    anguloX = brazo(anguloX - step*value)
    print(anguloX)
    kit.servo[15].angle = anguloX
    
def camY(value):
    global anguloY
    anguloY = brazo(anguloY + step*value)
    print(anguloY)
    kit.servo[14].angle = anguloY


#motor L
kit.continuous_servo[12].throttle = sp0
#motor R
kit.continuous_servo[13].throttle = sp0
#servo T (Y)
kit.servo[14].angle = anguloY
#servo P (X)
kit.servo[15].angle = anguloX

for event in gamepad.read_loop():

# Digitales
    
    if event.type == ecodes.EV_KEY:

#        if event.code == btn1:
#            if event.value == 1:
#                print('Pulsado btn1')
#            elif event.value == 0:
#                print('btn1 released')
                
        if event.code == btn4:
            if event.value != 0:
                print('Pulsado btn4')
                camY(-1)
            elif event.value == 0:
                print('btn4 released')
                
#        elif event.code == btn3:
#           if event.value == 1:
#               print('Pulsado btn3')
#           elif event.value == 0:
#               print('btn3 released')
                
                
        elif event.code == btn2:
            if event.value != 0:
                print('Pulsado btn2')
                camY(1)
            elif event.value == 0:
                print('btn2 released')
                
        elif event.code == btnR:
            if event.value != 0:
                print('Pulsado btnR')
                camX(1)
            elif event.value == 0:
                print('btnR released')
                
        elif event.code == btnL:
            if event.value != 0:
                print('Pulsado btnL')
                camX(-1)
            elif event.value == 0:
                print('btnL released')
                
        elif event.code == btnPlay:
            if event.value == 1:
                print('Pulsado btnPlay')
                brake()
            elif event.value == 0:
                print('btnPlay released')
                brake()
                
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
        if event.code == btnX:
            if event.value == -1:
                print('Pulsado L')
                rotateL()
            elif event.value == 1:
                print('Pulsado R')
                rotateR()
            else:
                print('R/L released')
                brake()
                
        elif event.code == btnY:
            if event.value != 0:
                print('pulsado up/down')
                forward(event.value)
            else:
                print('up/down released')
                brake()
