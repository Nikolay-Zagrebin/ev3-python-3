from ev3dev.ev3 import *

class motion:
    def __init__(self,gyro='in4',Ultrasonic='in1',motor_l='outA',motor_r='outC'):
        self.Gyro = GyroSensor(gyro)
        self.Ultra = UltrasonicSensor(Ultrasonic)
        self.Motor_L = LargeMotor(motor_l)
        self.Motor_R = LargeMotor(motor_r)    
    def getGyro(self):
        return self.Gyro.value()
    def getDist(self):
        return self.Ultra.value()        
    def motion_left(self,speed):
        self.Motor_L.run_timed(time_sp=3000,speed_sp=speed)
        self.Motor_R.run_timed(time_sp=3000,speed_sp=-speed)
    def motion_right(self,speed):
        self.Motor_L.run_timed(time_sp=3000,speed_sp=-speed)
        self.Motor_R.run_timed(time_sp=3000,speed_sp=speed)
    def motion_backward(self,speed):
        if(speed<0):
            speed=-speed
        self.Motor_L.run_timed(time_sp=3000,speed_sp=speed)
        self.Motor_R.run_timed(time_sp=3000,speed_sp=speed)
    def motion_forward(self,speed):
        if(speed>0):
            speed=-speed
        self.Motor_L.run_timed(time_sp=3000,speed_sp=speed)
        self.Motor_R.run_timed(time_sp=3000,speed_sp=speed)
    def motion_wheelspeed(self,sp1,sp2):
        if sp1>1000:
            sp1 = 1000
        elif sp1<-1000:
            sp1 = -1000

        if sp2>1000:
            sp2 = 1000
        elif sp2<-1000:
            sp2 = -1000

        self.Motor_L.run_timed(time_sp=3000,speed_sp=sp1)
        self.Motor_R.run_timed(time_sp=3000,speed_sp=sp2)
