#! /usr/bin/env python
# Main script for object detection and avoidance

# Core imports
import time
import ev3dev.ev3 as ev3
import os
import thread


# Local Imports
#import tutorial as tutorial
import utilities
import openLoopControl as o
import UScontrol as USC
import odometry as OC
from time import sleep
import FollowLine as FL


#print ('Welcome to ev3')

#ev3.Sound.speak('Welcome to EV3').wait()

osc=o.openLoopControl()
osc.operateMotors()
#motor2 =ev3.MediumMotor('outD'); assert motor2.connected
#motor0 = ev3.LargeMotor('outB'); assert motor0.connected
#motor1 = ev3.LargeMotor('outC'); assert motor1.connected
U=USC.UScontrol()
us=ev3.UltrasonicSensor()

ev3.Sound.speak('I am going to follow this line and avoid obstacles').wait()

#t_end = time.time() + 5
#while time.time() <  t_end:
while True:
    Follow=FL.FollowLine()
    Follow.Straight_PID_obstacle()
    obsDetect=USC.UScontrol()
    obsDetect.USscanForward_timed()
    #time.sleep(15)
    #obsDetect.USscanRight()
    #time.sleep(15)
    #obsDetect.USscanForward_timed2()
    #obsDetect.USscanRight()
    #obsDetect.USscanLeft()

#time.sleep(4)

# remove this if you want it to exit as soon as its done:
#print "wait 10sec, then end"
#time.sleep(10)
