from ev3dev.ev3 import * # library for controling ev3
from time import sleep 
import sys, termios, tty, os #for keyboard listening
 
 #method for listening for keys
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 

#initialising ultrasonic sensor
us = UltrasonicSensor() 
# Put the US sensor into distance mode.
us.mode='US-DIST-CM'
units = us.units

#motors initialisation
m = LargeMotor('outB')
a = LargeMotor('outC')
control=''



Sound.play('/home/robot/Beginning.wav').wait()#opening sound

print('Lets begin') #starting script takes few seconds. This just indicates when it is ready.

while control != 'q':
    distance = us.value()/10
    char = getch()
    if char == 'q':
        exit(0)
    elif char == 'e':
        Leds.set_color(Leds.LEFT, Leds.RED)
        Leds.set_color(Leds.RIGHT, Leds.RED)
        Sound.play('/home/robot/Exterminate.wav').wait()
        Leds.set_color(Leds.LEFT, Leds.YELLOW)
        Leds.set_color(Leds.RIGHT, Leds.YELLOW)
    elif char == 'm':
        Sound.play('/home/robot/MustSurvive.wav').wait()
    elif char == ' ' and distance < 20:
        print(str(distance) + " " + units)
        Sound.play('/home/robot/Exterminate.wav').wait()
    elif char == 'w':
        a.run_timed(time_sp=500, speed_sp=900)
        m.run_timed(time_sp=500, speed_sp=910)
    elif char == 's':
        a.run_timed(time_sp=500, speed_sp=-900)
        m.run_timed(time_sp=500, speed_sp=-900)
    elif char == 'a':
        a.run_timed(time_sp=140, speed_sp=200)
        m.run_timed(time_sp=140, speed_sp=-200)
    elif char == 'd':
        a.run_timed(time_sp=140, speed_sp=-200)
        m.run_timed(time_sp=140, speed_sp=200)
