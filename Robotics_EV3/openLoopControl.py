# For storing robot's state
# you can change the variables to store state in the class

import time
import math
import ev3dev.ev3 as ev3
import os


class openLoopControl():
    def __init__(self):
        # time in seconds
        self.time_to_spin = 0.25
        # Duty cycle (0-100)
        self.duty_cycle_sp = 10
        # position in degrees
        self.position_sp= 0
    

    def operateMotors(self):
        #Initialise all motors
        
        #Define power outlets
        print "spin the wheels"
        print str(self.time_to_spin) + " sec " 
        print str(self.duty_cycle_sp) + " power"
        print str(self.position_sp) + "degrees"
        print " "

        motor0 =ev3.LargeMotor('outB')
        motor1 =ev3.LargeMotor('outC')
        motor2 =ev3.MediumMotor('outD')
        motor0.connected
        motor1.connected
        motor2.connected

        # run_time takes milliseconds
        motor0.run_timed(duty_cycle_sp=self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) ) 
        motor0.run_timed(duty_cycle_sp= -self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) )
        motor1.run_timed(duty_cycle_sp=self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) ) 
        motor1.run_timed(duty_cycle_sp= -self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) )
        motor2.run_timed(duty_cycle_sp= -self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) )
        motor2.run_timed(duty_cycle_sp=self.duty_cycle_sp, time_sp=self.time_to_spin*1E3)
        time.sleep( math.ceil(self.time_to_spin) )
