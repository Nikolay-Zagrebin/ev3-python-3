#! /usr/bin/env python
# Core imports
#
#Our test script which we call the appropriate utility from.
##This program forms the main testing stream for calling test functions from the utilities class.

import time
import ev3dev.ev3 as ev3
import os
import thread
# Local Imports
import utilities as U
import openLoopControl as o
import UScontrol as USC
import odometry as OC
from time import sleep
import FollowLine as FL
import gyro as gyro


osc=o.openLoopControl()
osc.operateMotors()


#U.steeringLoop_timer()
#U.GyroTest()
#U.GyroTurn()
#U.turn_right()
#U.turn_left()
#U.UltraScan_360_test()
U.UltraScan_360_test()
#U.forward_distance_travel()

#g=gyro.GyroControl()
#g.GyroRead()

#g=ev3.GyroSensor()
#g.connected
#g.mode='GYRO-ANG'
#units=g.units
#while True:
#    print g.value()
#Scan for objects
