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
step=5
sp0 =0.15
anguloX = 90
anguloY = 0




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
        
def forward():
    kit.continuous_servo[13].throttle = speed
    kit.continuous_servo[12].throttle = -speed
    
def backward():
    kit.continuous_servo[13].throttle = -speed
    kit.continuous_servo[12].throttle = speed
    
def rotateL():
    kit.continuous_servo[13].throttle = speed
    kit.continuous_servo[12].throttle = sp0
    
def rotateR():
    kit.continuous_servo[13].throttle = sp0
    kit.continuous_servo[12].throttle = speed
           
def brake():
    kit.continuous_servo[13].throttle = sp0
    kit.continuous_servo[12].throttle = sp0
    

def camX(value):
    anguloX = brazo(anguloX + step)
    print(anguloX)
    kit.servo[15].angle = anguloX
    
def camY(value):
    anguloY = brazo(anguloY + step)
    print(anguloY)
    kit.servo[15].angle = anguloY


#motor L
kit.continuous_servo[12].throttle = sp0
#motor R
kit.continuous_servo[13].throttle = sp0
#servo T (X)
kit.servo[14].angle = anguloX
#servo P (Y)
kit.servo[15].angle = anguloY

for event in gamepad.read_loop():

# Digitales
    
    if event.type == ecodes.EV_KEY:

#        if event.code == btn1:
#            if event.value == 1:
#                print('Pulsado btn1')
#            elif event.value == 0:
#                print('btn1 released')
                
        if event.code == btn2:
            if event.value == 1:
                print('Pulsado btn2')
                backward()
            elif event.value == 0:
                print('btn2 released')
                brake()
                
#        elif event.code == btn3:
#           if event.value == 1:
#               print('Pulsado btn3')
#           elif event.value == 0:
#               print('btn3 released')
                
                
        elif event.code == btn4:
            if event.value == 1:
                print('Pulsado btn4')
                forward()
            elif event.value == 0:
                print('btn4 released')
                brake()
                
        elif event.code == btnR:
            if event.value == 1:
                print('Pulsado btnR')
                rotateR()
            elif event.value == 0:
                print('btnR released')
                brake()
                
        elif event.code == btnL:
            if event.value == 1:
                print('Pulsado btnL')
                rotateL()
            elif event.value == 0:
                print('btnL released')
                brake()
                
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
        if event.code == btnY:
            if event.value == -1:
                print('Pulsado up')
                camY(-1)
            elif event.value == 1:
                print('Pulsado down')
                camY(1)
            else:
                print('up/down released')
                
        elif event.code == btnX:
            if event.value == -1:
                print('Pulsado left')
                camX(-1)
            elif event.value == 1:
                print('Pulsado rigth')
                camX(1)
            else:
                print('rigth/left released')
