#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

USR = ev3.Sensor("in3", driver_name = "lego-ev3-us")
USR.mode = "US-DIST-CM"
USF = ev3.Sensor("in3", driver_name = "lego-ev3-us")
USF.mode = "US-DIST-CM"

#TO DO: redo a, b with centreLine and offseFromCentre in the code
a = 1
b = 2
centreLine = 2
offsetFromCentre = 1
x = 1
y = 2



'''
DISCLAIMER: USF is a side US sensor and USR is a rear US sensor.
Using both is an idea based around the use of trianglation, resulting in no need for a colour sensor.
However, if needed, we can just scrap the entire USF and use USR and CSv
'''

def USRCheck():
    USR.value = USRVal
    if USRVal > a:
        print("front")
        return 1
    elif USRVal < b:
        print("behind")
        return 2
    else:
        print("center")
        return 3
        

def USFCheck():
    USF.value = USFVal
    if USFVal > x:
        print("left")
        return 1
    elif USFVal < y:
        print("right")
        return 2
    else:
        print("center")
        return 3
