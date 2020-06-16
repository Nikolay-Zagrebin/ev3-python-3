#! /usr/bin/env python
# Core imports
#Alternative main script for curved line following which doesn't include the error ramp condition to handle tighter curves.
import time
import ev3dev.ev3 as ev3
import os
import thread


# Local Imports
#import tutorial as tutorial
import utilities
import openLoopControl as olc
import UScontrol as USC
import odometry as OC
from time import sleep
import FollowLine as FL


#print ('Welcome to ev3')

#ev3.Sound.speak('Welcome to EV3').wait()

ev3.Sound.speak('Hello,I am initialising my motors').wait()
#print("object at:"+str(sensor_value) + "mm")
#ev3.Sound.speak("object at"+str(motor2.position) + "degrees").wait()

o=olc.openLoopControl()
o.operateMotors()
#motor2 =ev3.MediumMotor('outD'); assert motor2.connected
#motor0 = ev3.LargeMotor('outB'); assert motor0.connected
#motor1 = ev3.LargeMotor('outC'); assert motor1.connected

ev3.Sound.speak('I am going to follow this line').wait()
Follow=FL.FollowLine()
Follow.curved_PID_forever2()
#time.sleep(4)

ev3.Sound.speak('I have finished following this line').wait()
# remove this if you want it to exit as soon as its done:
#print "wait 10sec, then end"
#time.sleep(10)
