#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor(INPUT_2)

m1 = LargeMotor("in1:i2c3:M1")
m2 = LargeMotor("in1:i2c3:M2")
m3 = LargeMotor(OUTPUT_A)
m4 = LargeMotor(OUTPUT_B)
m5 = MediumMotor(OUTPUT_C)
m6 = LargeMotor(OUTPUT_D)

print("Go")

while True:
    ts.wait_for_pressed()
    m1.run_forever(speed_sp=200)
    m2.run_forever(speed_sp=200)
    m3.run_forever(speed_sp=200)
    m4.run_forever(speed_sp=200)
    m5.run_forever(speed_sp=200)
    m6.run_forever(speed_sp=200)

    ts.wait_for_released()
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()
    m5.stop()
    m6.stop()

