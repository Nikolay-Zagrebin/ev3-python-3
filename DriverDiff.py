import ev3dev.ev3 as ev3
# TODO: Add code here
from time import sleep


l = ev3.LargeMotor('outA')
r = ev3.LargeMotor('outD')

def foward(d):
        t = 5.5 * d * 1000
        l.run_timed(time_sp=t, speed_sp=500)
        r.run_timed(time_sp=t, speed_sp=500)
        sleep(t/1000)
def rotate(dir):
        if(dir=='r'):
                l.run_timed(time_sp=1000, speed_sp=225)
                r.run_timed(time_sp=1000, speed_sp=-225)
        elif(dir=='l'):
                l.run_timed(time_sp=1000, speed_sp=-225)
                r.run_timed(time_sp=1000, speed_sp=225)
        sleep(1)
def circle():
        t = 9000
        l.run_timed(time_sp=t, speed_sp=1000)
        r.run_timed(time_sp=t, speed_sp=500)
        sleep(t/1000)
def half_circle(dir):
        t = 2200
        if(dir=='r'):
                l.run_timed(time_sp=t, speed_sp=800)
                r.run_timed(time_sp=t, speed_sp=250)
        elif(dir=='l'):
                l.run_timed(time_sp=t, speed_sp=250)
                r.run_timed(time_sp=t, speed_sp=800)
        sleep(float(t)/1000)
def eight():
        half_circle('r')



                r.run_timed(time_sp=1000, speed_sp=225)
        sleep(1)
def circle():
        t = 9000
        l.run_timed(time_sp=t, speed_sp=1000)
        r.run_timed(time_sp=t, speed_sp=500)
        sleep(t/1000)
def half_circle(dir):
        t = 2200
        if(dir=='r'):
                l.run_timed(time_sp=t, speed_sp=800)
                r.run_timed(time_sp=t, speed_sp=250)
        elif(dir=='l'):
                l.run_timed(time_sp=t, speed_sp=250)
                r.run_timed(time_sp=t, speed_sp=800)
        sleep(float(t)/1000)
def eight():
        half_circle('r')
        half_circle('l')
        half_circle('l')
        half_circle('r')
eight()
#for i in range (3):
#       for i  in range(4):
#               foward(0.5)
#C              rotate('r')

#print('esperei poha')
#l.run_timed(time_sp=3000,speed_sp=500)
