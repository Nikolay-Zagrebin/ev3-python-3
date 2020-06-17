#!/usr/bin/env python3
from motors import DriveBase, Picker
from sensors import RemoteControl
from simple_device import PowerSupply
from collections import defaultdict
import time

# # Configure the devices
remote = RemoteControl('in4')
base = DriveBase(left=('outC', DriveBase.POLARITY_INVERSED),
                 right=('outB', DriveBase.POLARITY_INVERSED),
                 wheel_diameter=4.3,
                 wheel_span=12,
                 counter_clockwise_is_positive=False)
      
picker = Picker('outA')
battery = PowerSupply()
print(battery.voltage)

# Dictionary of action tuples associated with remote button
actions = {
    'NONE' : (0,0,None),
    'LEFT_UP' : (0,40,None),
    'RIGHT_UP' : (0,-40,None),
    'BOTH_UP' : (6,0,None),
    'BOTH_DOWN' : (-6,0,None),
    'LEFT_DOWN' : (None, None, Picker.STORE),
    'RIGHT_DOWN' : (None, None, Picker.OPEN),
    'BEACON' : (None, None, Picker.PURGE)    
}

# Main Loop: Drive around and control picker based on remote
while True:
    try:
        speed_now, steering_now, target_now = actions[remote.button]
    except:
        speed_now, steering_now, target_now = actions['NONE']

    if target_now is not None:
        picker.go_to_target(target_now, blocking=True)
    if speed_now is not None and steering_now is not None:
        base.drive_and_turn(speed_now, steering_now)
    time.sleep(0.1)
