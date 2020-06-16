#!/usr/bin/python3

import time
import ev3dev.ev3 as ev3

m1 = ev3.LargeMotor('outA')
m2 = ev3.LargeMotor('outB')
m3 = ev3.LargeMotor('outD')
#m1.stop_action="hold"
#m1.stop_action="coast"
#m1.stop_action="brake"
m1.run_timed(time_sp=3000, speed_sp=500)
m2.run_timed(time_sp=3000, speed_sp=500)

# time is in ms
def go(time, speed):
  m1.run_timed(time_sp=time, speed_sp=speed)
  m2.run_timed(time_sp=time, speed_sp=speed)

go(1000*5, 500)
go(1000*5, 1000)
