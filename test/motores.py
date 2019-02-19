import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)
blue = GPIO.PWM(3,50)
blue.start(0)

try:
    while True:
        for i in range (0,101):
            blue.ChangeDutyCycle(i)
            sleep(0.02)
        for i in range (100,-1,-1):
            blue.ChangeDutyCycle(i)
            sleep(0.02)
            
except KeyboardInterrupt:
    pass

blue.stop()
GPIO.cleanup()
    
    