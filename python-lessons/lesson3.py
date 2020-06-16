#!/usr/bin/python3

import ev3dev.ev3 as ev3

range(0,10)  # this is a range object

# the speak function has no idea about ranges
ev3.Sound.speak(range(0,10)).wait()  

# we need to use for loop to ask EV3 to say numbers
# in the range
for k in range(0,10):
  ev3.Sound.speak(k).wait()  

for k in range(0,1):
  ev3.Sound.speak(k).wait()  

## the following will generate an error because only
## integers can be used in a range object!
for k in range(0,0.5):
  ev3.Sound.speak(k).wait()  

for k in range(0,0):
  ev3.Sound.speak(k).wait()
