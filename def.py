#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

#Моторы
leftmotor = LargeMotor("outA")
rightmotor = Largemotor("outB")


#Движение вперед
def straightahead(v, t):
    leftmotor.run_forever(speed_sp=v)
    rightmotor.run_forever(speed_sp=v)

    time.sleep(t)


#Поворот направо
def turnright():
    leftmotor.run_forever(speed_sp=200)
    rightmotor.run_forever(speed_sp=0)

    time.sleep(0.85)

#Основная программа
#Двигаемся вперед со скоростью 100, 3 сек.
straightahead(100, 3)

#Поворот направо
turnright()

#Прямо вперед
straightahead(250, 2)

#Снова направо
turnright()
