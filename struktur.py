#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

leftmotor = LargeMotor("outA")
rightmotor = LargeMotor("outB")

leftcs = ColorSensor("in1")
rightcs = ColorSensor("in2")
leftcs.mode = "COL-REFLECT"
rightcs.mode = "COL-REFLECT"

btn = Button()

knapp = TouchSensor("in3")

#Запускаем движки.
leftmotor.run_forever(speed_sp = 100)
rightmotor.run_forever(speed_sp = 100)

while(btn.any() == False):

    #Проверяем значения
    leftvalue = leftcs.value()
    rightvalue = rightcs.value()
    knappnedtryckt = knapp.value()

    if(knappnedtryckt == True):
        leftmotor.run_forever(speed_sp = 100)
        rightmotor.run_forever(speed_sp = 0)
        time.sleep(0.2)

    if(leftvalue < 20):
        leftmotor.run_forever(speed_sp = 50)
        rightmotor.run_forever(speed_sp = 100)

    elif(rightvalue < 20):
        leftmotor.run_forever(speed_sp = 100)
        rightmotor.run_forever(speed_sp = 50)

    if(rightvalue < 20 and leftvalue < 20):
        #Завершить цикл
        break

    time.sleep(0.01)

#Двигаемся вперед
leftmotor.run_forever(speed_sp = 100)
rightmotor.run_forever(speed_sp = 100)

#Новый цикл
while(btn.any() == False):

    leftmotor.run_forever(speed_sp = 100)
    rightmotor.run_forever(speed_sp = 100)

    #Проверяем значения
    knappnedtryckt = knapp.value()

    if(knappnedtryckt == True):
        leftmotor.run_forever(speed_sp = 100)
        rightmotor.run_forever(speed_sp = 0)
        time.sleep(0.8)

    time.sleep(0.01)
