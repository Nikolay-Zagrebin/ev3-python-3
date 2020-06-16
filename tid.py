#!/usr/bin/env python3
from ev3dev.ev3 import *
import time


b = Button()

#Ожидаем нажатия кнопки на брике
while(b.left == False):
    time.sleep(0.1)


#Сколько секунд прошло с 1 января 1970 года
starttid = time.time()

while(True):

    #Время итерации.
    tidnu = time.time()

    #Выводим принт через 3 секунды
    if(tidnu-starttid>3):
        print("do something")
        starttid = time.time()

    time.sleep(0.1)
