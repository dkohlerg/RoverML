from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)


from time import sleep

while True:

	kit.servo[14].angle = 180
	kit.servo[15].angle = 0
	sleep(1)
	kit.servo[14].angle = 0
	kit.servo[15].angle = 180
	sleep(1)


