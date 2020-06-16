#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

push = ev3.LargeMotor('outA')
right = ev3.LargeMotor('outB')
left = ev3.LargeMotor('outC')
cs = ev3.ColorSensor()
cs.mode = 'COL-COLOR'


def front_left2():
    right.run_forever(duty_cycle_sp=50, speed_sp=250)
    left.run_forever(duty_cycle_sp=50, speed_sp=20)
    time.sleep(1)
    right.stop()
    left.stop()
    push.run_forever(duty_cycle_sp=50, speed_sp=250)
    time.sleep(0.3)
    #push.stop()
    push.run_forever(duty_cycle_sp=50, speed_sp=-1000)
    time.sleep(0.3)
    push.run_to_rel_pos(position_sp = 20, speed_sp=400, stop_action="hold")
    #push.stop()
    right.run_forever(duty_cycle_sp=50, speed_sp=-500)
    left.run_forever(duty_cycle_sp=50, speed_sp=-250)
    time.sleep(0.)
    right.stop()
    left.stop()
    #push.stop()
    #time.sleep(0.2)
    return

def front_right2():
    right.run_forever(duty_cycle_sp=50, speed_sp=250)
    left.run_forever(duty_cycle_sp=50, speed_sp=500)
    time.sleep(0.5)
    right.stop()
    left.stop()
    #push.run_timed(time_sp=500, speed_sp=1000, stop_action='brake')
    push.run_forever(duty_cycle_sp=50, speed_sp=250)
    time.sleep(0.25)
    push.run_forever(duty_cycle_sp=50, speed_sp=-1000)
    time.sleep(0.3)
    push.run_to_rel_pos(position_sp = 20, speed_sp=400, stop_action="hold")
    #push.stop()
    right.run_forever(duty_cycle_sp=50, speed_sp=-250)
    left.run_forever(duty_cycle_sp=50, speed_sp=-500)
    time.sleep(0.41)
    right.stop()
    left.stop()
    #push.stop()
    #time.sleep(0.2)
    return


def black_block(muki):
    if muki == "r":
        right.run_timed(time_sp=200, speed_sp=-150, stop_action='brake')
        left.run_timed(time_sp=200, speed_sp=150, stop_action='brake')
    elif muki == "l":
        right.run_timed(time_sp=200, speed_sp=-150, stop_action='brake')
        left.run_timed(time_sp=200, speed_sp=150, stop_action='brake')

    push.run_forever(duty_cycle_sp=50, speed_sp=200)
    while cs.value != 0:
        right.run_timed(time_sp=600, speed_sp=-30, stop_action='hold')
        left.run_timed(time_sp=600, speed_sp=300, stop_action='hold')
        right.run_timed(time_sp=600, speed_sp=300, stop_action='hold')
        left.run_timed(time_sp=600, speed_sp=-30, stop_action='hold')
        #right.run_forever(duty_cycle_sp=50, speed_sp=200)
        #left.run_forever(duty_cycle_sp=50, speed_sp=200)
    right.stop()
    left.stop()
    while cs.value == 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=-100)
        left.run_forever(duty_cycle_sp=50, speed_sp=100)
    right.stop()
    left.stop()
    right.run_timed(time_sp=100, speed_sp=-150, stop_action='brake')
    left.run_timed(time_sp=100, speed_sp=150, stop_action='brake')
    push.stop()
    return

def kuro_turn_migi():
    left.run_forever(duty_cycle_sp=50, speed_sp=200)
    time.sleep(2)
    left.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=150)
        left.run_forever(duty_cycle_sp=50, speed_sp=250)
    right.stop()
    left.stop()
    right.run_timed(time_sp=200, speed_sp=200, stop_action='brake')
    left.run_timed(time_sp=200, speed_sp=200, stop_action='brake')
    while cs.value() == 6:
        right.run_forever(duty_cycle_sp=50, speed_sp=-100)
        left.run_forever(duty_cycle_sp=50, speed_sp=250)
    right.stop()
    left.stop()
    while 0 == cs.value() or cs.value()==6: #trace to color
        if cs.value() == 6:
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    return

def kuro_migi():
    left.run_forever(duty_cycle_sp=50, speed_sp=200)
    time.sleep(0.4)
    left.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=200)
        left.run_forever(duty_cycle_sp=50, speed_sp=200)
    right.stop()
    left.stop()
    right.run_timed(time_sp=200, speed_sp=300, stop_action='brake')
    left.run_timed(time_sp=200, speed_sp=-300, stop_action='brake')
    while 0 == cs.value() or cs.value() == 6:  # trace to color
        if cs.value() == 6:
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    return

def kuro_turn_hidari():
    right.run_forever(duty_cycle_sp=50, speed_sp=200)
    time.sleep(2)
    right.stop()
    while cs.value() != 0:
        left.run_forever(duty_cycle_sp=50, speed_sp=150)
        right.run_forever(duty_cycle_sp=50, speed_sp=250)
    left.stop()
    right.stop()
    left.run_timed(time_sp=200, speed_sp=200, stop_action='brake')
    right.run_timed(time_sp=200, speed_sp=-200, stop_action='brake')
    while 0 == cs.value() or cs.value() == 6:  # trace to color
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    left.stop()
    right.stop()
    return

def kuro_hidari():
    right.run_forever(duty_cycle_sp=50, speed_sp=200)
    time.sleep(0.4)
    right.stop()
    while cs.value() != 0:
        left.run_forever(duty_cycle_sp=50, speed_sp=200)
        right.run_forever(duty_cycle_sp=50, speed_sp=200)
    left.stop()
    right.stop()
    left.run_timed(time_sp=200, speed_sp=300, stop_action='brake')
    right.run_timed(time_sp=200, speed_sp=-300, stop_action='brake')
    while 0 == cs.value() or cs.value() == 6:  # trace to color
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    left.stop()
    right.stop()
    return

def trace(color):
    # blue 2, red 5, green 3, yel 4
    color1 = cs.value()
    pre = 0
    r_num = 0
    l_num = 0
    count = 0
    while color != color1:
        color1 = cs.value()
        #print(color1)
        if color1 != 6:
            right.run_forever(duty_cycle_sp=50, speed_sp=100)
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
        else: #if color1 == 6:
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
            left.run_forever(duty_cycle_sp=50, speed_sp=100)
    right.stop()
    left.stop()
    print(color1)
    return


def front_right():
    right.run_forever(duty_cycle_sp=50, speed_sp=200)
    left.run_forever(duty_cycle_sp=50, speed_sp=300)
    time.sleep(0.5)
    right.stop()
    left.stop()
    push.run_timed(time_sp=500, speed_sp=1000, stop_action='brake')
    push.stop()
    time.sleep(0.4)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    left.run_forever(duty_cycle_sp=50, speed_sp=-300)
    time.sleep(0.6)
    right.stop()
    left.stop()
    return


def front_left():
    right.run_forever(duty_cycle_sp=50, speed_sp=300)
    left.run_forever(duty_cycle_sp=50, speed_sp=200)
    time.sleep(0.5)
    right.stop()
    left.stop()
    push.run_timed(time_sp=500, speed_sp=1000, stop_action='brake')
    push.stop()
    time.sleep(0.3)
    right.run_forever(duty_cycle_sp=50, speed_sp=-300)
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(1)
    right.stop()
    left.stop()
    push.stop()
    return


def turn(has_block):
    if has_block:
        right.run_timed(time_sp=400, speed_sp=150, stop_action='brake')
        left.run_timed(time_sp=400, speed_sp=-150, stop_action='brake')
        while cs.value() != 0:
            right.run_forever(duty_cycle_sp=50, speed_sp=150)
            left.run_forever(duty_cycle_sp=50, speed_sp=-150)
        left.stop()
        right.stop()
    else:
        right.run_timed(time_sp=300, speed_sp=-400, stop_action='brake')
        left.run_timed(time_sp=300, speed_sp=-400, stop_action='brake')
        right.run_timed(time_sp=300, speed_sp=400, stop_action='brake')
        left.run_timed(time_sp=300, speed_sp=-400, stop_action='brake')
        while cs.value() != 0:
            right.run_forever(duty_cycle_sp=50, speed_sp=150)
            left.run_forever(duty_cycle_sp=50, speed_sp=-150)
        left.stop()
        right.stop()
    return

def turn_right():
    while cs.value() != 0:
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    left.stop()
    #right.run_timed(time_sp=500, speed_sp=-150, stop_action='brake')
    #left.run_timed(time_sp=500, speed_sp=500, stop_action='brake')

    while cs.value() != 6:
        #left.run_forever(duty_cycle_sp=50, speed_sp=300)
        #left.run_timed(time_sp=150, speed_sp=250, stop_action='brake')
        #right.run_timed(time_sp=150, speed_sp=250, stop_action='brake')
        left.run_forever(duty_cycle_sp=50, speed_sp=250)
        right.run_forever(duty_cycle_sp=50, speed_sp=250)

    right.stop()
    left.stop()
    while cs.value() != 0:
        left.run_forever(duty_cycle_sp=50, speed_sp=-100)
        right.run_forever(duty_cycle_sp=50, speed_sp=100)

    #left.stop()

    #left.run_timed(time_sp=150, speed_sp=150, stop_action='brake')
    #right.run_timed(time_sp=150, speed_sp=-50, stop_action='brake')
    left.stop()
    right.stop()
    return

def turn_left():
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
    while cs.value() != 6:
        right.run_forever(duty_cycle_sp=50, speed_sp=-100)
    left.stop()
    right.stop()
    return


def front_left_jump():
    time1 = time.time()
    while int(time.time() - time1) < 1:
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.25)
    left.stop()
    right.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.2)
    left.stop()
    right.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.12)
    left.stop()
    right.stop()
    push.run_forever(duty_cycle_sp=50, speed_sp=800)
    time.sleep(0.3)
    push.stop()
    time.sleep(0.3)

    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=-100)
        left.run_forever(duty_cycle_sp=50, speed_sp=-100)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.2)
    left.stop()
    right.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.3)
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=-200)
        left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.stop()
    left.stop()
    #left.run_forever(duty_cycle_sp=50, speed_sp=-300)
    #right.run_forever(duty_cycle_sp=50, speed_sp=-300)
    #time.sleep(0.1)
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.25)
    left.stop()
    right.stop()
    return

def nasi():
    left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.run_forever(duty_cycle_sp=50, speed_sp=300)
    time.sleep(0.15)
    left.stop()
    right.stop()

def front_right_jump():
    time1 = time.time()
    while int(time.time() - time1) < 1:
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.25)
    left.stop()
    right.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.2)
    left.stop()
    right.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.12)
    left.stop()
    right.stop()
    push.run_forever(duty_cycle_sp=50, speed_sp=800)
    time.sleep(0.3)
    push.stop()
    time.sleep(0.3)
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=-100)
        left.run_forever(duty_cycle_sp=50, speed_sp=-100)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.2)
    left.stop()
    right.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.3)
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=-200)
        left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=350)
    right.run_forever(duty_cycle_sp=50, speed_sp=350)
    time.sleep(0.2)
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.15)
    left.stop()
    right.stop()
    return


def jump_left():
    time1 = time.time()
    while int(time.time() - time1) < 1:
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=300)
    time.sleep(0.3)
    left.stop()
    right.stop()

    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.run_forever(duty_cycle_sp=50, speed_sp=300)
    time.sleep(0.2)
    left.stop()
    right.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-100)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.3)
    left.stop()
    right.stop()
    return


def jump_right():
    time1 = time.time()
    while int(time.time() - time1) < 1:
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.35)
    left.stop()
    right.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    right.run_timed(time_sp=200, speed_sp=-300, stop_action='brake')
    left.run_timed(time_sp=200, speed_sp=400, stop_action='brake')
    return


def jump():
    time1 = time.time()
    while int(time.time() - time1) < 1:
        if cs.value() == 6:
            left.run_forever(duty_cycle_sp=50, speed_sp=120)
            right.run_forever(duty_cycle_sp=50, speed_sp=200)
        else:
            left.run_forever(duty_cycle_sp=50, speed_sp=200)
            right.run_forever(duty_cycle_sp=50, speed_sp=120)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=400)
    right.run_forever(duty_cycle_sp=50, speed_sp=-200)
    time.sleep(0.3)
    left.stop()
    right.stop()
    #right.run_timed(time_sp=300, speed_sp=-100, stop_action='brake')
    #left.run_timed(time_sp=300, speed_sp=100, stop_action='brake')
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=-200)
    right.run_forever(duty_cycle_sp=50, speed_sp=400)
    time.sleep(0.5)
    left.stop()
    right.stop()
    while cs.value() != 0:
        right.run_forever(duty_cycle_sp=50, speed_sp=300)
        left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.stop()
    left.stop()
    left.run_forever(duty_cycle_sp=50, speed_sp=300)
    right.run_forever(duty_cycle_sp=50, speed_sp=-100)
    time.sleep(0.3)
    left.stop()
    right.stop()

    right.run_timed(time_sp=200, speed_sp=-100, stop_action='brake')
    left.run_timed(time_sp=200, speed_sp=100, stop_action='brake')
    return
