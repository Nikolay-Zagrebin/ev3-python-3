#!/usr/bin/env pybricks-micropython
import sys
from threading import Thread

from pybricks.ev3devices import ColorSensor, Motor, TouchSensor
from pybricks.hubs import EV3Brick
from pybricks.messaging import (BluetoothMailboxClient, NumericMailbox, TextMailbox)
from pybricks.parameters import Color, Port, Button
from pybricks.media.ev3dev import SoundFile, Image, ImageFile, Font
from pybricks.tools import wait

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

MASTER_BRICK='master'

# Create your objects here.
ev3 = EV3Brick()
roll_head = Motor(Port.A)
yaw_base = Motor(Port.B)

roll_head.control.limits(1400,3600,100)
yaw_base.control.limits(1400,1400,100)

client = BluetoothMailboxClient()
commands_bt_text = TextMailbox('commands text', client)
roll_head_bt_zeroing = NumericMailbox('zero position roll', client)
roll_head_bt_num = NumericMailbox('roll head degree', client)
roll_head_bt_sp = NumericMailbox('roll head speed', client)
roll_head_feedb = NumericMailbox('roll head feedback', client)
yaw_base_bt_zeroing = NumericMailbox('zero position yaw', client)
yaw_base_bt_num = NumericMailbox('yaw base degree', client)
yaw_base_bt_sp = NumericMailbox('yaw base speed', client)
yaw_base_feedb = NumericMailbox('yaw base feedback', client)


# Write your program here.
ev3.speaker.set_volume(volume=80, which='_all_')
ev3.speaker.beep()
ev3.light.off()                 #Turn the lights off on the brick

client.connect(MASTER_BRICK)

def move_yaw_base():
    while True:
        yaw_base_bt_num.wait_new()
        yaw_base.run_target(yaw_base_bt_sp.read(), yaw_base_bt_num.read(), wait=False)

def move_roll_head():
    while True:
        roll_head_bt_num.wait_new()
        roll_head.run_target(roll_head_bt_sp.read(), roll_head_bt_num.read(), wait=False)

def control_check():
    if yaw_base.control.done() and roll_head.control.done():
        commands_bt_text.send("No movement")
        wait(100)
    else:
        commands_bt_text.send("Moving")
        wait(100)

def angle_feedback():
    while True:
        yaw_base_feedb.send(yaw_base.angle())
        roll_head_feedb.send(roll_head.angle())
        wait(250)

sub_yaw_base = Thread(target=move_yaw_base)
sub_roll_head = Thread(target=move_roll_head)
sub_angle_feedback = Thread(target=angle_feedback)
sub_yaw_base.start()
sub_roll_head.start()
sub_angle_feedback.start()

ev3.screen.load_image(ImageFile.EV3_ICON)
ev3.light.on(Color.ORANGE)

while True:
    buttons = ev3.buttons.pressed()
    if Button.CENTER in buttons:
        break
    elif Button.UP in buttons:
        yaw_base.run(500)
    elif Button.DOWN in buttons:
        yaw_base.run(-500)
    elif Button.LEFT in buttons:
        roll_head.run(-500)
    elif Button.RIGHT in buttons:
        roll_head.run(500)
    else:
        yaw_base.hold()
        roll_head.hold()
    wait(100)

yaw_base.hold()
roll_head.hold()
ev3.light.off()                                 #Turn the lights off on the brick

yaw_base.reset_angle(-25)
roll_head.reset_angle(-40)

# while commands_bt_text.read() != 'Initiate yaw base':
#     wait(100)
# commands_bt_text.send('Initiated yaw base')


while commands_bt_text.read() != 'Initiate roll head':
    wait(100)
commands_bt_text.send('Initiated roll head')

wait(1000)

while True:
    try:
        control_check()
    except OSError:
        print('SLAVE> Lost connection to master brick, shutting down...')
        sys.exit(0)

    wait(10)
