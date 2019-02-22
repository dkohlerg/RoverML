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
sp0 =0.15

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
    

#motor L
kit.continuous_servo[12].throttle = sp0
#motor R
kit.continuous_servo[13].throttle = sp0
#servo T (Y)
kit.servo[14].angle = 180
#servo P (X)
kit.servo[15].angle = 90

for event in gamepad.read_loop():

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
