#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from threading import Thread
import bluetooth
import bluetooth

mB = LargeMotor('outB')
mC = LargeMotor('outC')
mD = MediumMotor('outD')

cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode='RGB-RAW'  # set mode to measure color ID

btn=Button()


def communicate_with_server():
    global run, count, warehouse_num, temp1, temp2, humi1, humi2 
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)
    
    count_temp = -1
    print("Beginning to connect with server")
    while True:
        try:
            client_sock, address = server_sock.accept()
            break
        except:
            continue
    
    print("Accepted connection from ", address) 
    
    client_sock.send('t')
    client_sock.send(str(temp1))
    client_sock.send(str(humi1))
    client_sock.send(str(temp2))
    client_sock.send(str(humi2))
    client_sock.send(str(warehouse_num))
    
    while True:
        if client_sock.recv(1).decode('utf-8') == 'g':
            run = True
            client_sock.send('r')
            print("run ok")
            print(run)
            break
    while True:
        if client_sock.recv(1).decode('utf-8') == 'r':
            break       
    
    while run:
        if count == 14:
            client_sock.send('0')
            client_sock.send('s')
            break
        elif count != count_temp:
            client_sock.send(str(count))
            count_temp = count

    client_sock.close()
    server_sock.close()



def buttonStop():
    global run # so that we can use the same global variable 'run'
    # that we created in the main script below
    while btn.any()==False:  # while no button is pressed
        sleep(0.01)  # do nothing other than wait
    run=False  # Set run to False to cause loop below to stop.
    Sound.beep()

# Create a global variable 'run' which will be set to
# False when we want the thread above to stop running.
global run
run = False

global count
count = 0
count_add = 1
en = True

t1 = Thread(target=buttonStop)
t1.start()


global warehouse_num, temp1, temp2, humi1, humi2
warehouse_num = 2
temp1 = 10
humi1 = 10
temp2 = 20
humi2 = 20 

t2 = Thread(target=communicate_with_server)
t2.start()

mD.run_to_rel_pos(position_sp=45, speed_sp=100)
sleep(1)
warehouse_point = warehouse_num + 4
print(warehouse_point)

while not run:
    continue

while run:
    # turn left if white 
    red = cl.value(0)
    green = cl.value(1) 
    blue = cl.value(2)
    
    # The speed of two Large motor
    a = (red+green+blue)//3
    b = 255 - a
    
    R = red - (blue+green)//2
    #G = green - (red+blue)//2
    B = blue - red #(red+green)//2
    #print("R: " + str(R) + ", G: " + str(G)+ ", B: " + str(B))
    #print("count: "+ str(count))
    if count >= 14:
        mB.stop()
        mC.stop()
        run = False
    else:
        if B >= 100: # arrive blue point
            count += count_add
            mB.stop()
            mC.stop()
            sleep(1)
            mD.run_to_rel_pos(position_sp=-45, speed_sp=100)
            sleep(3)
            mB.run_timed(time_sp=5000, speed_sp=10)
            mC.run_timed(time_sp=5000, speed_sp=100)
            sleep(5)
        
        
        elif R >= 100: # arrive red point
            if en == True:
                count += count_add
                count_add = 1
                en = False
                if count == warehouse_point:
                    mB.stop()
                    mC.stop()
                    mB.run_timed(time_sp=2500, speed_sp=100)
                    mC.run_timed(time_sp=2500, speed_sp=-30)
                    sleep(2.5)
                    continue
                elif count == 4 or count == 6:
                    count_add = 2
            
            mB.run_forever(speed_sp=80)
            mC.run_forever(speed_sp=80)
        else:
            en = True
            '''
            distance = us.value()
            print(distance)
            if distance <= 150: # less than 15.0cm
                mB.run_timed(time_sp=2000, speed_sp=80)
                mC.run_timed(time_sp=2000, speed_sp=0)
                sleep(2)
                mB.run_timed(time_sp=5000, speed_sp=50)
                mC.run_timed(time_sp=5000, speed_sp=100)
                sleep(5)
                mB.run_timed(time_sp=1000, speed_sp=100)
                mC.run_timed(time_sp=1000, speed_sp=50)
                sleep(1)
                
            else:
            '''
            mB.run_forever(speed_sp=b*0.6)
            mC.run_forever(speed_sp=a*0.6)
if not run:
     mB.stop()
     mC.stop()
     sleep(1)  
    # Do nothing while we're waiting, then stop the robot.
