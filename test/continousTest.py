from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep

while True:

	kit.continuous_servo[15].throttle = 0.5
	sleep(1)
	kit.continuous_servo[15].throttle = -0.5
	sleep(1)
	if (input().readline == ' '):
		kit.continous_servo[15].throttle = 0
