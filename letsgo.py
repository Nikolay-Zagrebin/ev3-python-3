#!/usr/bin/env python3
#Импорт библиотеки
from ev3dev.ev3 import *
import time

leftmotor = LargeMotor("outA")
#leftmotor = LargeMotor("in1:i2c3:M2")

#Запустите двигатель со скоростью 360 градусов в секунду.
leftmotor.run_forever(speed_sp=360)

#Ждем 3 секунды
time.sleep(3)

#Стопорим мотор
leftmotor.stop(stop_action="hold")
