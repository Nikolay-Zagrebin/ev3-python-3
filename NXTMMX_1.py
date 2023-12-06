#!/usr/bin/env pybricks-micropython

from pybricks.tools import wait
import os

for item in os.listdir("/sys/class/tacho-motor"):
    rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
    address = rpn.read()
    address = address.replace("\n", "")
    rpn.close()
    print(item + " found as: " + address)


#   ev3-ports:in1:i2c3:M2
#            "in1:i2c3:M2"
TACHO_MOTOR = (
    "/sys/class/tacho-motor/motor4/"
)


def write_tacho(attr, value):
    with open(TACHO_MOTOR + attr, "w") as f:
        f.write(value + "\n")


def print_tacho(attr):
    with open(TACHO_MOTOR + attr, "r") as f:
        print(f.read().strip())


# # Resetting the Motor

# write_tacho("command", "reset")

# # Position and Speed

# print_tacho("position") # looking at the position attribute
# write_tacho("position", "0") # reset position

# Now, turn the motor one rotation by hand and read the position again…

#print_tacho("position")
#print_tacho("count_per_rot")

# Running the Motor

# print_tacho("commands") # To find out what commands are available

print("run-forever")
# write_tacho("speed_sp", "500")
# write_tacho("command", "run-forever")
# wait(10000)

# write_tacho("speed_sp", "-1000")
# write_tacho("command", "run-forever")
# wait(10000)
# write_tacho("command", "stop")

print("run-to-abs-pos")
# write_tacho("command", "run-to-abs-pos")
# wait(10000)

print("run-to-rel-pos")
# write_tacho("position_sp", "180")
# write_tacho("command", "run-to-rel-pos")
# wait(10000)

print("run-timed")
# write_tacho("time_sp", "2000")
# write_tacho("command", "run-timed")

# Не поддерживается
print("run-direct")
# write_tacho("duty_cycle_sp", "20")
# write_tacho("command", "run-direct")
# wait(10000)

# Stopping the Motor
print_tacho("stop_actions") # To find out what stop_actions are available

print("coast")
# write_tacho("speed_sp", "1000")
# write_tacho("time_sp", "1000")
# write_tacho("stop_action", "coast")
# write_tacho("command", "run-timed")
# wait(10000)

print("brake")
# write_tacho("speed_sp", "1000")
# write_tacho("time_sp", "1000")
# write_tacho("stop_action", "brake")
# write_tacho("command", "run-timed")
# wait(10000)

print("hold")
# write_tacho("speed_sp", "1000")
# write_tacho("position_sp", "180")
# write_tacho("stop_action", "hold")
# write_tacho("command", "run-to-rel-pos")
wait(10000)

# Polarity
print_tacho("polarity")

# write_tacho("polarity", "inversed")
# write_tacho("speed_sp", "300")
# write_tacho("command", "run-forever")
# for _ in range(100):
#     print_tacho("position")
#     wait(10)
