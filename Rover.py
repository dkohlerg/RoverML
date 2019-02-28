
class Rover:

    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)

     ## CONSTRUCTOR

    def __init__(self,speed,step,sp0,agX,agY):
        self.speed=speed
        self.step=step
        self.sp0=sp0
        self.agX=agX
        self.agY=agY
        #motor L
        kit.continuous_servo[12].throttle = sp0
        #motor R
        kit.continuous_servo[13].throttle = sp0
        #servo T (Y)
        kit.servo[14].angle = agY
        #servo P (X)
        kit.servo[15].angle = agX


     ## METODOS PARA EL MOVIMIENTO DE LOS MOTORES PRINCIPALES

    def mmFW(self):
        kit.continuous_servo[13].throttle = -speed
        kit.continuous_servo[12].throttle = speed

    def mmBW(self):
        kit.continuous_servo[13].throttle = speed
        kit.continuous_servo[12].throttle = -speed

    def mmFWL(self):
        kit.continuous_servo[13].throttle = -speed
        kit.continuous_servo[12].throttle = 0.5*speed

    def mmFWR(self):
        kit.continuous_servo[13].throttle = -0.5*speed
        kit.continuous_servo[12].throttle = speed

    def stp(self):
        kit.continuous_servo[13].throttle = sp0
        kit.continuous_servo[12].throttle = sp0



     ## METODOS PARA EL MOVIMIENTO DE LA CAMARA

    def cmL(value):
        global agX
        agX = brazo(agX + step)
        kit.servo[15].angle = agX

    def cmR(value):
        global agX
        agX = brazo(agX - step)
        kit.servo[15].angle = agX

    def cmUP(value):
        global agY
        agY = brazo(agY - step)
        kit.servo[15].angle = agY

    def cmDW(value):
        global agY
        agY = brazo(agY + step)
        kit.servo[15].angle = agY