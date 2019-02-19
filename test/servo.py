from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as gpio
import time

gamepad=InputDevice('/dev/input/event3')

print(gamepad)

gpio.setmode(gpio.BOARD)

gpio.setup(3, gpio.OUT)

step = 0.1
dC=6
servo  = gpio.PWM(3,50)
servo.start(dC)

# Codigo de botones

btn1=304
btn2=305
btn3=307
btn4=308

def normalizeDC(a):
    
    if a > 13:
        return 13
    elif a < 2:
        return 2
    else:
        return a

try:

        for event in gamepad.read_loop():

                if (event.code == btn1):
                    dC = normalizeDC(dC + event.value * step)
                    servo.ChangeDutyCycle(dC)
                                    
                elif (event.code == btn2):
                    dC=normalizeDC(dC - event.value * step)
                    servo.ChangeDutyCycle(dC)


except KeyboardInterrupt:
    servo.stop()
    gpio.cleanup()
    
    

