# Copyright 2019 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
# 
# You may not use this file except in compliance with the terms and conditions 
# set forth in the accompanying LICENSE.TXT file.
#
# THESE MATERIALS ARE PROVIDED ON AN "AS IS" BASIS. AMAZON SPECIFICALLY DISCLAIMS, WITH 
# RESPECT TO THESE MATERIALS, ALL WARRANTIES, EXPRESS, IMPLIED, OR STATUTORY, INCLUDING 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

import time
import logging
import threading
import random

from agt import AlexaGadget

from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, LargeMotor, OUTPUT_A, MediumMotor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, MediumMotor
# Set the logging level to INFO to see messages from AlexaGadget
logging.basicConfig(level=logging.INFO)
import json

class MindstormsGadget(AlexaGadget):
    """
    A Mindstorms gadget that performs movement in sync with music tempo.
    """

    def __init__(self):
        """
        Performs Alexa Gadget initialization routines and ev3dev resource allocation.
        """
        super().__init__()

        # Ev3dev initialization
        self.leds = Leds()
        self.sound = Sound()
        self.left_motor = LargeMotor(OUTPUT_B)
        self.right_motor = LargeMotor(OUTPUT_C)
        self.hand_motor = MediumMotor(OUTPUT_A)
        # Gadget states
        self.bpm = 0
        self.trigger_bpm = "off"
        self.drive = MoveTank(OUTPUT_B, OUTPUT_C)
        self.weapon = MediumMotor(OUTPUT_A)




    def on_connected(self, device_addr):
        """
        Gadget connected to the paired Echo device.
        :param friendly_name: the friendly name of the gadget that has connected to the echo device
        """
        self.leds.set_color("LEFT", "GREEN")
        self.leds.set_color("RIGHT", "GREEN")
        print("{} connected to Echo device".format(self.friendly_name))

    def on_disconnected(self, device_addr):
        """
        Gadget disconnected from the paired Echo device.
        :param friendly_name: the friendly name of the gadget that has disconnected from the echo device
        """
        self.leds.set_color("LEFT", "BLACK")
        self.leds.set_color("RIGHT", "BLACK")
        print("{} disconnected from Echo device".format(self.friendly_name))

    def on_custom_mindstorms_gadget_control(self, directive):
        """
        Handles the Custom.Mindstorms.Gadget control directive.
        :param directive: the custom directive with the matching namespace and name
        """
        try:
            payload = json.loads(directive.payload.decode("utf-8"))
            print("Control payload: {}".format(payload))
            control_type = payload["type"]
            if control_type == "spin":
                print("Move command found")
                self.hand_motor.run_timed(speed_sp=1050, time_sp=2500)
            if control_type == "movef":
                print("Move Forward command found")
                self.right_motor.run_timed(speed_sp=1050, time_sp=1000)
                self.left_motor.run_timed(speed_sp=1050, time_sp=1000)
            if control_type == "moveb":
                print("Move backward command found")
                self.right_motor.run_timed(speed_sp=-1050, time_sp=1000)
                self.left_motor.run_timed(speed_sp=-1050, time_sp=1000)
            if control_type == "mover":
                print("Move right command found")
                self.right_motor.run_timed(speed_sp=-1050, time_sp=1000)
                self.left_motor.run_timed(speed_sp=1050, time_sp=1000)
            if control_type == "movel":
                print("Move left command found")
                self.right_motor.run_timed(speed_sp=1050, time_sp=1000)
                self.left_motor.run_timed(speed_sp=-1050, time_sp=1000)
            

            if control_type == "command":
                self.hand_motor.run_timed(speed_sp=1050, time_sp=2500)
        except KeyError:
            print("Missing expected parameters: {}".format(directive))


    def on_alexa_gadget_musicdata_tempo(self, directive):
        """
        Provides the music tempo of the song currently playing on the Echo device.
        :param directive: the music data directive containing the beat per minute value
        """
        tempo_data = directive.payload.tempoData
        for tempo in tempo_data:

            print("tempo value: {}".format(tempo.value))
            if tempo.value > 0:
                # dance pose
                self.right_motor.run_timed(speed_sp=750, time_sp=2500)
                self.left_motor.run_timed(speed_sp=-750, time_sp=2500)
                self.hand_motor.run_timed(speed_sp=750, time_sp=2500)
                self.leds.set_color("LEFT", "GREEN")
                self.leds.set_color("RIGHT", "GREEN")
                time.sleep(3)
                # starts the dance loop
                self.trigger_bpm = "on"
                threading.Thread(target=self._dance_loop, args=(tempo.value,)).start()

            elif tempo.value == 0:
                # stops the dance loop
                self.trigger_bpm = "off"
                self.leds.set_color("LEFT", "BLACK")
                self.leds.set_color("RIGHT", "BLACK")

    def on_alexa_gadget_statelistener_stateupdate(self, directive):
        """
        Listens for the wakeword state change and react by turning on the LED.
        :param directive: contains a payload with the updated state information from Alexa
        """
        color_list = ['BLACK', 'AMBER', 'YELLOW', 'GREEN']
        for state in directive.payload.states:
            if state.name == 'wakeword':

                if state.value == 'active':
                    print("Wake word active - turn on LED")
                    self.sound.play_song((('A3', 'e'), ('C5', 'e')))
                    for i in range(0, 4, 1):
                        self.leds.set_color("LEFT", color_list[i], (i * 0.25))
                        self.leds.set_color("RIGHT", color_list[i], (i * 0.25))
                        time.sleep(0.25)

                elif state.value == 'cleared':
                    print("Wake word cleared - turn off LED")
                    self.sound.play_song((('C5', 'e'), ('A3', 'e')))
                    for i in range(3, -1, -1):
                        self.leds.set_color("LEFT", color_list[i], (i * 0.25))
                        self.leds.set_color("RIGHT", color_list[i], (i * 0.25))
                        time.sleep(0.25)



    def _dance_loop(self, bpm):
        """
        Perform motor movement in sync with the beat per minute value from tempo data.
        :param bpm: beat per minute from AGT
        """
        color_list = ["GREEN", "RED", "AMBER", "YELLOW"]
        led_color = random.choice(color_list)
        motor_speed = 400
        milli_per_beat = min(1000, (round(60000 / bpm)) * 0.65)
        print("Adjusted milli_per_beat: {}".format(milli_per_beat))
        while self.trigger_bpm == "on":

            # Alternate led color and motor direction
            led_color = "BLACK" if led_color != "BLACK" else random.choice(color_list)
            motor_speed = -motor_speed

            self.leds.set_color("LEFT", led_color)
            self.leds.set_color("RIGHT", led_color)
            self.right_motor.run_timed(speed_sp=motor_speed, time_sp=150)
            self.left_motor.run_timed(speed_sp=-motor_speed, time_sp=150)
            time.sleep(milli_per_beat / 1000)

        print("Exiting BPM process.")


if __name__ == '__main__':
    # Startup sequence
    gadget = MindstormsGadget()
    gadget.sound.play_song((('C4', 'e'), ('D4', 'e'), ('E5', 'q')))
    gadget.leds.set_color("LEFT", "GREEN")
    gadget.leds.set_color("RIGHT", "GREEN")

    # Gadget main entry point
    gadget.main()

    # Shutdown sequence
    gadget.sound.play_song((('E5', 'e'), ('C4', 'e')))
    gadget.leds.set_color("LEFT", "BLACK")
    gadget.leds.set_color("RIGHT", "BLACK")
