#! /usr/bin/env python
# Core imports
import time
import ev3dev.ev3 as ev3
import os
import thread


# Local Imports
#import tutorial as tutorial
import utilities
#import openLoopControl as olc
import UScontrol as USC
import odometry as OC
from time import sleep


U=USC.UScontrol()
ev3.Sound.speak('Scanning for objects').wait()

us=ev3.UltrasonicSensor()

#sensor_value = 200
    
while(us.value() > 100):
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanRight()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    U.USscanLeft()
    print us.value()
    pass
sensor_value=us.value()
motor2.stop

ev3.Sound.speak('Object has been detected').wait()
print("object at:"+str(sensor_value) + "mm")
ev3.Sound.speak("object at"+str(motor2.position) + "degrees").wait()
