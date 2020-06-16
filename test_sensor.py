#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

#Кнопки на брике
btn = Button()

#моторы
leftmotor = LargeMotor("outA")
rightmotor = LargeMotor("outB")

#сенсор кнопка
knapp = TouchSensor("in3")

def stop():
    leftmotor.stop(stop_action="hold")
    rightmotor.stop(stop_action="hold")

#Поворот вправо
def turnright():
    leftmotor.run_forever(speed_sp=200)
    rightmotor.run_forever(speed_sp=0)

    time.sleep(0.85)
    stop()


def testbutton():
    #Ждем нажатия кнопки
    while(btn.left == False):

        #Если нажали поворачиваем вправо
        if(knapp.value() == True):
            turnright()
            leftmotor.run_forever(speed_sp=200)
            rightmotor.run_forever(speed_sp=200)

        time.sleep(0.1)

#Запускаем
leftmotor.run_forever(speed_sp=200)
rightmotor.run_forever(speed_sp=200)
testbutton()
