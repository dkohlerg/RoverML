from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

from time import sleep

kit.continuous_servo[15].throttle = 0
