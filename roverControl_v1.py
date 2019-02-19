from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
from evdev import InputDevice, categorize, ecodes
gamepad=InputDevice('/dev/input/event0')
print(gamepad)
kit = ServoKit(channels=16)

# Codigo de botones

sp=1
step=5

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

analogRx=3
analogRy=4
analogLx=0
analogLy=1

global anguloX
anguloX = 90
global anguloY
anguloY = 90
defSpeed =0.15


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
    kit.continuous_servo[13].throttle = sp -defSpeed
    kit.continuous_servo[12].throttle = -sp + defSpeed
def backwards(a):
    kit.continuous_servo[13].throttle = -sp*a + defSpeed
    kit.continuous_servo[12].throttle = sp*a - defSpeed
def rotateL(a):
    kit.continuous_servo[13].throttle = sp*a - defSpeed
    kit.continuous_servo[12].throttle = defSpeed
def rotateR(a):
    kit.continuous_servo[13].throttle = defSpeed
    kit.continuous_servo[12].throttle = sp*a - defSpeed

    
def brake():
    kit.continuous_servo[13].throttle = defSpeed
    kit.continuous_servo[12].throttle = defSpeed
def camY(value):
    global anguloX
    anguloX =brazo(anguloX + step * value)
    kit.servo[14].angle =anguloX

def camX(value):
    global anguloY
    anguloY =brazo( anguloY + step * value)
    print(anguloY)
    kit.servo[15].angle = anguloY


#motor L
kit.continuous_servo[12].throttle = defSpeed
#motor R
kit.continuous_servo[13].throttle = defSpeed
#servo T (X)
kit.servo[14].angle = 90
#servo P (Y)
kit.servo[15].angle = 0

for event in gamepad.read_loop():
    if event.code == btn4:
        print('alante '+ str(event.value))
        forward(event.value)
        print('estoy en brake')
        
    elif event.code == btn2:
        print('atras')
        backwards(event.value)
    elif event.code == btnL:
        print('L')
        rotateL(event.value)

    elif event.code == btnR:
        print('R')
        rotateR(event.value)

    elif event.code == btnPlay:
        print('br')
        brake()

    elif event.code == btnX:
        print('X'+ str(event.value))
        camX(event.value)

    elif event.code == btnY:
        print('Y' + str(event.value))
        camY(event.value)
