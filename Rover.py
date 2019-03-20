class Rover(object):

    from adafruit_servokit import ServoKit
    ## CONSTRUCTOR

    def __init__(self,speed,step,sp0,agX,agY,kit): 
        self.speed=speed
        self.step=step
        self.sp0=sp0
        self.agX=agX
        self.agY=agY
        self.kit=kit
        #motor L
        #kit.continuous_servo[12].throttle = sp0
        #motor R
        #kit.continuous_servo[13].throttle = sp0
        #servo T (Y)
        kit.servo[14].angle = agY
        #servo P (X)
        kit.servo[15].angle = agX


     ## METODOS PARA EL MOVIMIENTO DE LOS MOTORES PRINCIPALES

    def mmFW(self):
         self.kit.continuous_servo[13].throttle = self.speed
         self.kit.continuous_servo[12].throttle = -self.speed

    def mmBW(self):
        self.kit.continuous_servo[13].throttle = -self.speed
        self.kit.continuous_servo[12].throttle = self.speed

    def mmFWL(self):
        self.kit.continuous_servo[13].throttle = self.speed
        self.kit.continuous_servo[12].throttle = self.sp0

    def mmFWR(self):
        self.kit.continuous_servo[13].throttle = self.sp0
        self.kit.continuous_servo[12].throttle = -self.speed

    def stp(self):
        self.kit.continuous_servo[13].throttle = self.sp0
        self.kit.continuous_servo[12].throttle = self.sp0



     ## METODOS PARA EL MOVIMIENTO DE LA CAMARA
     ## TODO

    def cmL(self):
        if ((self.agX + self.step) < 180):
            self.agX=self.agX + self.step
            self.kit.servo[15].angle = self.agX

    def cmR(self):
        if ((self.agX - self.step) > 0):
            self.agX=self.agX - self.step
            self.kit.servo[15].angle = self.agX


    def cmUP(self):
        if (self.agY - self.step) > 70:
            self.agY=self.agY - self.step
            self.kit.servo[14].angle = self.agY

    def cmDW(self):
        if (self.agY + self.step) < 180:
            self.agY=self.agY + self.step
            self.kit.servo[14].angle = self.agY

