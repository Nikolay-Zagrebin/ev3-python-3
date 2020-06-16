#! /usr/bin/env python
#
# Class for controlling the servoing of the ultrasonic sensor.
# Can implement object avoidance if necessary
#
import time
import math
import ev3dev.ev3 as ev3
import utilities as util
import FollowLine as FL
import odometry as OC



class UScontrol():
    def __init__(self):
        # time in seconds
        self.time_to_spin = 0.25
        # Duty cycle (0-100)
        self.duty_cycle_sp = 10
        
    def USscanRight(self):
        #print "scanning for objects"
        us=ev3.UltrasonicSensor()            
        motor2 =ev3.MediumMotor('outD')
        motor2.connected
        motor2.run_timed(time_sp=1000, speed_sp=90)
        sensor_value =us.value()
        
        #print us.value()
        ev3.Sound.speak('Object detected').wait()
        print("object at:"+str(sensor_value) + "mm")
        ev3.Sound.speak("object at"+str(motor2.position) + "degrees").wait()
        
        #print('sleeping for 1 second')
        time.sleep(1)

    def USscanLeft(self):
        #print "scanning for objects"

        #NB speed_sp is in degrees per second.             
        motor2 =ev3.MediumMotor('outD')
        motor2.connected
        motor2.run_timed(time_sp=2000, speed_sp=-90)
        #motor2.run_timed(time_sp=2000, speed_sp=-90)

        #print('sleeping for 1 second')
        time.sleep(1)

    def USscanComplete(self):      
        motor2 =ev3.MediumMotor('outD')
        motor2.connected
        motor2.run_timed(time_sp=2000, speed_sp=-90)
        us=ev3.UltrasonicSensor()
        while(us.value() > 50):
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=-90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=-90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=-90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=-90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=90)
            print us.value()
            motor2.run_timed(time_sp=2000, speed_sp=90)
        pass
        sensor_value=us.value()
        motor2.stop
        ev3.Sound.speak('Object has been detected').wait()
        print("object at:"+str(sensor_value) + "mm")
        ev3.Sound.speak("object at"+str(motor2.position) + "degrees").wait()

    def USscanForward_timed(self):
        #This function scans for objects and implements avoidance measures
        #if necessary
                    
        motor2 =ev3.MediumMotor('outD')
        motor2.connected
        
        #motor2.run_timed(time_sp=2000, speed_sp=-90)
        us=ev3.UltrasonicSensor()
        #t_end = time.time() + 5
        #while time.time() <  t_end:
        print us.value()
        if us.value() < 100:
            ev3.Sound.speak('object detected').wait()
            OD=OC.OdometryControl()
            OD.turn_left_ObjectAvoid()
            motor2.run_timed(time_sp=1000, speed_sp= 90)
            OD.objectAvoidForward()
            motor2.run_timed(time_sp=1000, speed_sp= 90)
            ev3.Sound.speak('object still in range').wait()
            motor2.run_timed(time_sp=1000, speed_sp= -90)
            motor2.run_timed(time_sp=1000, speed_sp= -90)
            OD.turn_right_ObjectAvoid()
            OD.objectAvoidForward()
            OD.turn_right_ObjectAvoid()
            OD.objectAvoidForward2()
            ev3.Sound.speak('object has been avoided')      


def USscanForward_timed2(self):
        #This function scans for objects and implements avoidance measures
        #if necessary
                    
        motor2 =ev3.MediumMotor('outD')
        motor2.connected
        
        #motor2.run_timed(time_sp=2000, speed_sp=-90)
        us=ev3.UltrasonicSensor()
        #t_end = time.time() + 5
        #while time.time() <  t_end:
        print us.value()
        if us.value() < 100:
            ev3.Sound.speak('object still in range').wait()
            OD=OC.OdometryControl()
            #OD.turn_left_ObjectAvoid()
            #OD.objectAvoidForward()
            OD.turn_right_ObjectAvoid()
            OD.objectAvoidForward()
            OD.turn_right_ObjectAvoid()
            OD.objectAvoidForward2()
            
                
                
            
            #motor2.run_timed(time_sp=2000, speed_sp=90)
        #time.sleep(1)
