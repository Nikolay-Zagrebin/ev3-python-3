#! /usr/bin/env python
#This script forms the primary program run for PID curved line following

# Core imports
import time
import ev3dev.ev3 as ev3
import os
import thread


# Local Imports
import utilities
import openLoopControl as olc
import UScontrol as USC
import odometry as OC
from time import sleep
import FollowLine as FL


#print ('Welcome to ev3')

ev3.Sound.speak('Hello I am initialising motors').wait()

o=olc.openLoopControl()
o.operateMotors()
#motor2 =ev3.MediumMotor('outD'); assert motor2.connected
#motor0 = ev3.LargeMotor('outB'); assert motor0.connected
#motor1 = ev3.LargeMotor('outC'); assert motor1.connected

ev3.Sound.speak('I am going to follow this line').wait()

t_end = time.time() + 25
while time.time() <  t_end:
    Follow=FL.FollowLine()
    Follow.curved_PID_timed()
ev3.Sound.speak('I have finished following this curved line').wait()

#time.sleep(4)

# remove this if you want it to exit as soon as its done:
#print "wait 10sec, then end"
#time.sleep(10)
