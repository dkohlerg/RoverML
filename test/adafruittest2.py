from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

from time import sleep

try:

	while True:

		for i in range (0,181):

			sleep(0.01)
			kit.servo[15].angle = i
			kit.servo[14].angle = 180-i

		for i in range (0,181):

			sleep(0.01)
			kit.servo[14].angle = i
			kit.servo[15].angle = 180-i

except KeyboardInterrupt:
	exit()
