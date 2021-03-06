#!/usr/bin/env python3

__author__ = 'anton'

import evdev
import ev3dev.auto as ev3
import threading
import time
from collections import deque

#Helpers
def clamp(n, range):
    """
    Given a number and a range, return the number, or the extreme it is closest to.
    :param n: number
    :return: number
    """
    minn, maxn = range
    return max(min(maxn, n), minn)


def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    val: float or int
    src: tuple
    dst: tuple
    example: print scale(99, (0.0, 99.0), (-1.0, +1.0))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scalestick(value):
    return scale(value,(0,255),(-100,100))

print("Finding ps3 controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if device.name == 'PLAYSTATION(R)3 Controller':
        ps3dev = device.fn


gamepad = evdev.InputDevice(ps3dev)



side_speed = 0
turn_speed = 0
fwd_speed = 0
running = True
gyro_assist = 0
circle_button_pressed = 0

class MotorThread(threading.Thread):
    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.tail_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.tail_motor.run_direct(duty_cycle_sp = -40)
        self.tail_motor.wait_until("stalled")
        self.tail_motor.stop()
        self.tail_motor.position = 0
        self.gyro = ev3.GyroSensor(ev3.INPUT_1)
        self.gyro.mode = ev3.GyroSensor.MODE_GYRO_RATE
        self.gyro.auto_mode = False
        self.offset = 0
        for i in range(60):
            self.offset += self.gyro.rate
            time.sleep(0.015)
        self.offset /= 100
        threading.Thread.__init__(self)
        self.rates = deque([0]*4, maxlen=4)

    def run(self):
        print("Engines running!")
        while running:
            try: # Some bug in Ev3dev can cause this to crash
                self.rates += [self.gyro.rate - self.offset]
            except:
                pass

            rate=(self.rates[0]+self.rates[3])/2

            left_motor_dc = clamp((fwd_speed + side_speed / 3) + rate * gyro_assist * 0.3, (-100, 100))
            right_motor_dc = clamp((fwd_speed - side_speed / 3) + rate * gyro_assist * 0.3, (-100, 100))

            self.left_motor.run_direct(duty_cycle_sp=left_motor_dc)
            self.right_motor.run_direct(duty_cycle_sp=right_motor_dc)

            tail_motor_target = circle_button_pressed * 360
            tail_motor_error = self.tail_motor.position - tail_motor_target
            if -10 < tail_motor_error < 10:
                tail_motor_error = 0
            self.tail_motor.run_direct(duty_cycle_sp= -clamp(tail_motor_error, (-100, 100)))

            time.sleep(0.015)
        self.left_motor.stop()
        self.right_motor.stop()
        self.tail_motor.stop()


if __name__ == "__main__":
    motor_thread = MotorThread()
    motor_thread.setDaemon(True)
    motor_thread.start()

    for event in gamepad.read_loop(): #this loops infinitely
        if event.type == 3: #A stick is moved

            if event.code == 0: #X axis on left stick
                side_speed = scalestick(event.value)

            if event.code == 1: #Y axis on left stick
                fwd_speed = scalestick(event.value)


        if event.type == 1:
            if event.code == 300:
                if event.value == 1:
                    triangle_pressed_time = time.time()
                if event.value == 0 and time.time() > triangle_pressed_time + 0.5:
                    print("Triangle button is pressed. Break.")
                    running = False
                    time.sleep(0.5) # Wait for the motor thread to finish
                    break

            elif event.code == 301:
                circle_button_pressed = event.value

            elif event.code == 302:
                if event.value == 1:
                    cross_pressed_time = time.time()
                if event.value == 0 and time.time() > cross_pressed_time + 0.5:
                    if gyro_assist:
                        gyro_assist = 0
                    else:
                        gyro_assist = 1
                    print("X button. Switch gyro to {0}".format(gyro_assist))
