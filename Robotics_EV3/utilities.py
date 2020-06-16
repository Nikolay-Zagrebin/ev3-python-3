#! /usr/bin/env python
#
# Utility class. Build any test functions in here to be called from the test
#program.

import time
import ev3dev.ev3 as ev3
from time import sleep

# Local Imports
import utilities
import openLoopControl as olc
import UScontrol as USC
import odometry as OC


# Get time in milliseconds
def timestamp_now (): return int (time.time () * 1E3)


       

    
def steeringLoop_timer():
    #This function times the loop iteration duration 
    #We use this value as dT for discrete PID or PD control

    motor2 =ev3.MediumMotor('outD')
    motor0 = ev3.LargeMotor('outB'); assert motor0.connected
    motor1 = ev3.LargeMotor('outC'); assert motor1.connected


    # Connect EV3 color sensor.
    cl = ev3.ColorSensor() 

    # Put the color sensor into COL-REFLECT mode
    # to measure reflected light intensity.
    cl.mode='COL-REFLECT'
    #t_end = time.time() + 7


    Kp = 250                     
    Ki = 0  
    Kd = 0                       
    offset = 85                         
    Tp = 25
    integral = 0                          
    lastError =  0                        
    derivative = 0                        
    total = []                             #Initialise array to store times
    for times in range(100):              #Number of loop iterations        
        start = time.time()
        LightValue = cl.value()            
        error = LightValue - offset        
        integral = integral + error         
        derivative = error - lastError     
        Turn = Kp*error + Ki*integral + Kd*derivative 
        Turn = Turn/100                      
        powerA = Tp + Turn                 
        powerC = Tp - Turn                 
        motor0.run_forever(speed_sp=powerA, duty_cycle_sp=25)
        motor1.run_forever(speed_sp=powerC,duty_cycle_sp=25 )
        lastError = error                 
        stop = time.time()
        duration = stop - start
        total.append(duration)              #append loop time for this iteration to array
        print(duration)
    average = sum(total) / len(total)      # calculate the average value
    print("this is the average",average)   # print the average

    


def GyroTest():
               
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        print(units)
        while True:
            start_value = g.value()
            print("start value is: ",start_value)
            motor0.run_timed(time_sp=3000, speed_sp=50)
            motor1.run_timed(time_sp=3000, speed_sp=-50)
            sleep(5)
            end_value = g.value()
            print("end value is: ",end_value)
            sleep(5)
            start_value = g.value()
            print("start value is: ",start_value)
            motor0.run_timed(time_sp=3000, speed_sp=-50)
            motor1.run_timed(time_sp=3000, speed_sp=50)
            sleep(5)
            end_value = g.value()
            print("end value is: ",end_value)

def GyroTurn():

        #Turn through 90 degrees and back and print starting and ending values
    
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        print(g.value())
        #print(units)
        #start_value = abs(g.value())
        #print(start_value)
        #target_value = abs(abs(g.value()) + 90)
        while g.value() <= 90:
            motor0.run_forever(speed_sp=50, duty_cycle_sp=25)
            motor1.run_forever(speed_sp=-50,duty_cycle_sp=25)
            print(g.value())
        while g.value() >= 0:
            motor0.run_forever(speed_sp=-50, duty_cycle_sp=25)
            motor1.run_forever(speed_sp=50,duty_cycle_sp=25)
            print(g.value())  
        
        
def turn_right():
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=5000, speed_sp=50, duty_cycle_sp=25)
        motor1.run_timed(time_sp=5000, speed_sp=-50, duty_cycle_sp=25)
        sleep(3)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

def turn_left():
        g=ev3.GyroSensor()
        g.connected
        g.mode='GYRO-ANG'
        units=g.units
        read_start = g.value()
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=5000, speed_sp=-50, duty_cycle_sp=25)
        motor1.run_timed(time_sp=5000, speed_sp=50, duty_cycle_sp=25)
        sleep(3)
        read_end = g.value()
        print("start angle of rotation "+str(read_start)+" degrees")
        print("end angle of rotation "+str(read_end)+" degrees")

def forward_distance_travel():
        motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        read_start = motor0.position
        motor0.run_timed(time_sp=2000, speed_sp=100, duty_cycle_sp=25)
        motor1.run_timed(time_sp=2000, speed_sp=100, duty_cycle_sp=25)
        sleep(11)
        read_end = motor0.position
        print("start rotation"+str(read_start)+"degrees")
        print("End rotation"+str(read_end)+"degrees")

def forward():
    
    motor0 = ev3.LargeMotor('outB');  assert motor0.connected
    motor1 = ev3.LargeMotor('outC'); assert motor1.connected
    motor0.run_direct(duty_cycle_sp=75)
    motor1.run_direct(duty_cycle_sp=75)


def UltraScan_360_test():
    import UltraSensor
    
    
    



# fill in others here e.g.
# wheelTicsToMetres()
# driveForwardMetres(distance)
