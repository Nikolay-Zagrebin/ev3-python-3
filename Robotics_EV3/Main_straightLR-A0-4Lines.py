#! /usr/bin/env python
#
#Main script for segmented line following. Uses A0 size odometry
#
# Core imports
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

ev3.Sound.speak('Hello,I am initialising motors').wait()
#print("object at:"+str(sensor_value) + "mm")
#ev3.Sound.speak("object at"+str(motor2.position) + "degrees").wait()

o=olc.openLoopControl()
o.operateMotors()
#motor2 =ev3.MediumMotor('outD'); assert motor2.connected
#motor0 = ev3.LargeMotor('outB'); assert motor0.connected
#motor1 = ev3.LargeMotor('outC'); assert motor1.connected


ev3.Sound.speak('I am going to follow these lines').wait()
Follow=FL.FollowLine()
Follow.Straight_PD_timed()
#time.sleep(4)
ev3.Sound.speak('I have reached the end of first line').wait()
OD=OC.OdometryControl()
OD.turn_right()
OD.forward()
ev3.Sound.speak('I have reached the second line').wait()
Follow=FL.FollowLine()
Follow.Straight_PD2_timed()
ev3.Sound.speak('I have reached the end of second line').wait()
OD=OC.OdometryControl()
OD.turn_left()
OD.forward2()
OD.turn_right()
ev3.Sound.speak('I have reached the third line').wait()
Follow=FL.FollowLine()
Follow.Straight_PD4_timed()
ev3.Sound.speak('I have reached the end of the third line').wait()
OD=OC.OdometryControl()
OD.turn_right()
OD.forward()
ev3.Sound.speak('I have reached the fourth line').wait()
Follow=FL.FollowLine()
Follow.Straight_PD2_timed()
ev3.Sound.speak('I have reached the end of fourth line').wait()
OD=OC.OdometryControl()
OD.turn_left()
OD.forward2()
OD.turn_right()
ev3.Sound.speak('I have reached the final line').wait()
Follow=FL.FollowLine()
Follow.Straight_PD3_timed()
ev3.Sound.speak('I have reached the end of the final line').wait()

# remove this if you want it to exit as soon as its done:
#print "wait 10sec, then end"
#time.sleep(10)
