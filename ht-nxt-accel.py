#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound
from ev3dev2.button import *
import time

from ev3dev2.led import Leds

# Lego NXT Sound Sensor
#https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensor_data.html#lego-nxt-sound
# import - no idea   from ev3dev2.sensor import *

from ev3dev2.sensor.lego import SoundSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.port import LegoPort
from time import sleep

p = LegoPort(INPUT_4)
p.set_device = 'lego-nxt-sound'

sleep(1)

s = SoundSensor()
s.mode = 'DB'

# HiTechnic Accelerometer for NXT
a = Sensor(address=INPUT_1, driver_name='ht-nxt-accel')
a.mode = 'ALL'

# David Lechner help
#debug_print(c.address)
#value = a.value
#debug_print(value)

us = UltrasonicSensor(INPUT_3)
#ts = TouchSensor(INPUT_1)
#a = Accelerometer(INPUT_1)
#cl = ColorSensor('in4')
sound = Sound()
leds = Leds()

lm = LargeMotor(OUTPUT_A)

sound.set_volume(100)
sound.speak("Let us use the accelerometer")
sound.set_volume(50)
sound.speak("Half the volume")

leds.animate_rainbow()
running = True
while(running):

    dist_cm = us.distance_centimeters
    print(dist_cm)

    #print(a.value())

    value = a.value
    #x,y,z = a.value
    print("Accel:" + str(value))


    # got to get x, y and  z

    # or just use msb if last two bits are not important
    x, y, z, *_ = a.bin_data("<6b") # David Lechner help
    print("X:" + str(x))
    print("Y:" + str(y))
    print("Z:" + str(z))

    db = s.sound_pressure

    print("db Level:" + str(db))
    time.sleep(1)


    # lower the units louder the INPUT to SoundSensor
    if db < 25:
        sound.play_song((('D4', 'e3'),('D4', 'e3'),('D4', 'e3'),('G4', 'h'),('D5', 'h')))

        time.sleep(3)
        lm.run_timed(time_sp=1000, speed_sp=-300)
        time.sleep(3)



    #loc = a.get_acceleration()
    #print(loc.x, loc.y, loc.z)

    if (dist_cm < 15):
        print ("Time to run the motor")
        lm.run_timed(time_sp=1500, speed_sp=720)
