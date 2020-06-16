#! /usr/bin/env python
#
# Main odometry class for storing odometry task functions.

import time
import math
import ev3dev.ev3 as ev3
import utilities as util
import UScontrol as US
from time import sleep



class OdometryControl():
    def __init__(self):
        #motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        #motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        # time in seconds
        #self.time_to_spin = 0.25
        #Duty cycle (0-100)
        #self.duty_cycle_sp = 10
        time_sp=2000
        duty_cycle_sp=75

    def forward(self):
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=8000, speed_sp=50, duty_cycle_sp=25)
        motor1.run_timed(time_sp=8000, speed_sp=50, duty_cycle_sp=25)
        sleep(8)
        read_end = motor0.position
        print("start rotation"+str(read_start)+"degrees")
        print("End rotation"+str(read_end)+"degrees")
        

    def forward2(self):
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=12500, speed_sp=40, duty_cycle_sp=25)
        motor1.run_timed(time_sp=12500, speed_sp=40, duty_cycle_sp=25)
        sleep(13)
        read_end = motor0.position
        print("start rotation"+str(read_start)+"degrees")
        print("End rotation"+str(read_end)+"degrees")

    def objectAvoidForward(self):
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=5000, speed_sp=40, duty_cycle_sp=25)
        motor1.run_timed(time_sp=5000, speed_sp=40, duty_cycle_sp=25)
        sleep(5)
        read_end = motor0.position
        print("start rotation"+str(read_start)+"degrees")
        print("End rotation"+str(read_end)+"degrees")

    def objectAvoidForward2(self):
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=6000, speed_sp=50, duty_cycle_sp=25)
        motor1.run_timed(time_sp=6000, speed_sp=50, duty_cycle_sp=25)
        sleep(6)
        read_end = motor0.position
        print("start rotation"+str(read_start)+"degrees")
        print("End rotation"+str(read_end)+"degrees")

    

    def back(self):
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=8000, speed_sp=-100, duty_cycle_sp=25)
        motor1.run_timed(time_sp=8000, speed_sp=-100, duty_cycle_sp=25)
        sleep(5)
        read_end = motor0.position
        print("start rotation "+str(read_start)+" degrees")
        print("End rotation "+str(read_end)+" degrees")
        
    def turn_right(self):
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=2000, speed_sp=49, duty_cycle_sp=50)
        motor1.run_timed(time_sp=2000, speed_sp=-49, duty_cycle_sp=50)
        sleep(2)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

    def turn_left(self):
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=3000, speed_sp=-40, duty_cycle_sp=25)
        motor1.run_timed(time_sp=3000, speed_sp=40, duty_cycle_sp=25)
        sleep(3)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

    def turn_left_ObjectAvoid(self):
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=2500, speed_sp=-45, duty_cycle_sp=25)
        motor1.run_timed(time_sp=2500, speed_sp=45, duty_cycle_sp=25)
        sleep(3)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

    def turn_right_ObjectAvoid(self):
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=3000, speed_sp=45, duty_cycle_sp=25)
        motor1.run_timed(time_sp=3000, speed_sp=-45, duty_cycle_sp=25)
        sleep(2)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

    def Gyro_only(self):
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        while True:
            read_start = g.value()
            print str(read_start)

    def Scan_Right(self):
        us=US.UScontrol()
        us.USscanRight()
