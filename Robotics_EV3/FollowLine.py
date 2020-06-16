# This class contains functions for controlling line following tasks.
#  *._timed -- Control function that runs for a specified time interval
# *._forever -- Control function that will run indefinately or until an interupt occurs.
# *._obstacle -- Control function which is utilised for the object avoidance task.
# PD -- Proportional, derivative
# PID proportional,integral,derivative
# 

import time
import math 
import ev3dev.ev3 as ev3
import utilities as util
import time



class FollowLine():
    def __init__(self):
        #motor0 = ev3.LargeMotor('outB');  assert motor0.connected
        #motor1 = ev3.LargeMotor('outC'); assert motor1.connected
        # time in seconds
        #self.time_to_spin = 0.25
        #Duty cycle (0-100)
        #self.duty_cycle_sp = 10
        time_sp=10000
        #duty_cycle_sp=75
        #motor2 =ev3.MediumMotor('outD'); assert motor2.connected
               
                
    def Straight_PD_timed(self):
        #Initialise motors
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected

             
        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 13


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 0                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 50
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
            
            LightValue = cl.value()            # current light reading?
            error = LightValue - offset        # subtract the offset
            integral = integral + error        # calculate the integral 
            derivative = error - lastError     # calculate the derivative
            Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
            Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
            powerA = Tp + Turn                 # power level for A motor
            powerC = Tp - Turn                 # power level for C motor
            motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
            motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
            lastError = error                  # save error for next time around loop
           
    def Straight_PD2_timed(self):
        #This function has a longer time duration

        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 16


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 0                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 50
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop


    
    def Straight_PD3_timed(self):
        #Initialise motors

        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 4


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 0                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 50
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop



    def Straight_PD4_timed(self):
        #This is used in the 5 line version(2 x A0 sheets) of Task B
        
        #Initialise motors
        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 16


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 0                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 50
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop
       
   


    def Straight_PD_forever(self):
        #Initialise motors

        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        #t_end = time.time() + 7


        Kp = 120                     # scaled by 10 to cater for small value integer arithmetic
        Ki = 5  
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 25
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while True:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_forever(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_forever(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop
           if error >= 15:                    # Stops ramp condition and servos the right wheel backwards to correct error on tight curves.
               error=15
               motor0.run_timed(speed_sp=-25,duty_cycle_sp=25)
              
           
           #lastError = error                  # save error for next time around loop




    def curved_PID_forever2(self):
        #This function doesn't use the error limiting loop for controlling tight
        #turns

        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        #t_end = time.time() + 7


        Kp = 120                     # scaled by 10 to cater for small value integer arithmetic
        Ki = 5  
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 40
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while True:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_forever(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_forever(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop

    def curved_PID_timed(self):
        #This function has a longer time duration

        #motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 60


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 5                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 50
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop
           #if error >= 15:                    # Stops ramp condition and servos the right wheel backwards to correct error on tight curves.
               #error=15
              #motor0.run_timed(speed_sp=-25,duty_cycle_sp=25)

    def Straight_PID_obstacle(self):
        #Initialise motors

        motor2 =ev3.MediumMotor('outD')
        motor0 = ev3.LargeMotor('outB'); assert motor0.connected
        motor1 = ev3.LargeMotor('outC'); assert motor1.connected


        # Connect EV3 color sensor.
        cl = ev3.ColorSensor() 

        # Put the color sensor into COL-REFLECT mode
        # to measure reflected light intensity.
        cl.mode='COL-REFLECT'
        t_end = time.time() + 9


        Kp = 120                      # scaled by 10 to cater for small value integer arithmetic
        Ki = 5                          # scaled by 10 to cater for small value integer arithmetic
        Kd = 100                       # scaled by 10 to cater for small value integer arithmetic
        offset = 85                         # Initialize the variables
        Tp = 40
        integral = 0                          
        lastError =  0                        
        derivative = 0                        

        while time.time() < t_end:
           LightValue = cl.value()            # current light reading?
           error = LightValue - offset        # subtract the offset
           integral = integral + error        # calculate the integral 
           derivative = error - lastError     # calculate the derivative
           Turn = Kp*error + Ki*integral + Kd*derivative #the "P term" the "I term" and the "D term"
           Turn = Turn/100                      # undo the affect of the factor of 100 in Kp, Ki and Kd!
           powerA = Tp + Turn                 # power level for A motor
           powerC = Tp - Turn                 # power level for C motor
           motor0.run_timed(speed_sp=powerA, duty_cycle_sp=25)
           motor1.run_timed(speed_sp=powerC,duty_cycle_sp=25 )
           lastError = error                  # save error for next time around loop
