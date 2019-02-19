from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
from time import sleep
from evdev import InputDevice, categorize, ecodes
gamepad=InputDevice('/dev/input/event0')
print(gamepad)
kit = ServoKit(channels=16)

# Cdsadodigo de botones

sp=0.5
step=0.05

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

global anguloY
anguloY = 0


def camX(value):
	global anguloY
	anguloY =anguloY + step * value
	print(anguloY)
	kit.continuous_servo[13].throttle = anguloY


#motor R
kit.continuous_servo[13].throttle = 0
#motor L
kit.continuous_servo[12].throttle = 0
#servo T (X)
kit.servo[14].angle = 90
#servo P (Y)
kit.servo[15].angle = 90

for event in gamepad.read_loop():
	if event.code == btn4:
		print('alante')
		forward(event.value)

	if event.code == btn2:
		print('atras')
		backwards(event.value)

	if event.code == btnL:
		print('L')
		rotateL(event.value)

	if event.code == btnR:
		print('R')
		rotateR(event.value)

	if event.code == btnPlay:
		print('br')
		brake()

	if event.code == btnX:
		print('X'+ str(event.value))
		camX(event.value)

	if event.code == btnY:
		print('Y' + str(event.value))
		camY(event.value)
