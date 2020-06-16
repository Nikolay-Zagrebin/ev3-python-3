#! /usr/bin/env python3
# Core imports
import time
import sys
import ev3dev.ev3 as ev3
import ev3dev.core as ev3core

 
def open_food_container(food_container,direction):
	
	if direction  == 'left':
		food_container.run_to_rel_pos(position_sp=80,speed_sp=300)
		time.sleep(0.2)
		food_container.run_to_rel_pos(position_sp=-80,speed_sp=300)
	
	if direction  == 'right':
		food_container.run_to_rel_pos(position_sp=80,speed_sp=300)
		time.sleep(0.2)
		food_container.run_to_rel_pos(position_sp=-80,speed_sp=-300)

def open_chute_hatch(chute_hatch):	
	chute_hatch.run_to_rel_pos(position_sp=80,speed_sp=300)
	time.sleep(0.5)
	chute_hatch.run_timed(speed_sp=-200,time_sp=700)

def rotate_chute(chute,direction):	
	time.sleep(1.0)
	if direction == '1':
		chute.run_timed(speed_sp=-200,time_sp=250)
		time.sleep(2.0)
		

	if direction == '2':
		chute.run_timed(speed_sp=200, time_sp=200)
		time.sleep(2.0)
	
	time.sleep(1.0)	

def return_chute(chute,direction):
	time.sleep(1.0)
	if direction == '1':
		chute.run_timed(speed_sp=200,time_sp=200)
		time.sleep(2.0)

	if direction == '2':
		chute.run_timed(speed_sp=-200,time_sp=200)
		time.sleep(2.0)


if __name__ == '__main__':

	bowl = sys.argv[1]	
	right_food_container = ev3.LargeMotor('outA')
	left_food_container = ev3.LargeMotor('outD') 
	weighing_chamber = ev3.LargeMotor('outC')
	chute = ev3.LargeMotor('outB')	
	
	open_food_container(right_food_container, 'right')
	open_food_container(left_food_container,'left')
	open_chute_hatch(weighing_chamber)
	rotate_chute(chute,bowl)
	return_chute(chute,bowl)
