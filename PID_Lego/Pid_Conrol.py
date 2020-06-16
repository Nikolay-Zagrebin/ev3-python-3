from ev3dev.ev3 import *
import os,time
import pid
import sys
import Motion
# os.system('espeak -s 120 -v zh \'woyaoshiyong\' --stdout|aplay')
# os.system('espeak -s 120 -v en-us \'p i d\' --stdout|aplay')
# os.system('espeak -s 120 -v zh \'suanfa\' --stdout|aplay')

# pid= pid.PID(P=sys.argv[1],I=sys.argv[2],D=sys.argv[3])
pid=pid.PID(P=0.2,I=0.2,D=0.3)
motion = Motion.motion()


pid.setPoint(0.0)

def Pid_Adjast(move_speed,isforward):
    angle=motion.getGyro()
    pid.update(angle)
    out = int(abs(pid.output*10))

    print "angle:"+str(angle)
    print "out:"+str(out)

    if angle>=5:
        motion.motion_wheelspeed(-move_speed,-move_speed-out)
    elif angle<= -5:
        motion.motion_wheelspeed(-move_speed-out,-move_speed)
    else:
        pass

def Nor_Adjast():
    angle=motion.getGyro()
    if angle>=5:
        motion.motion_left(1000)
    elif angle<=-5:
        motion.motion_right(1000)
    else:
        pass

move_speed = 300

while True:
    time.sleep(1)
    motion.motion_forward(move_speed)

    # if motion.getDist()<100:
    #     Nor_Adjast()
    # else:
    Pid_Adjast(move_speed,True)
