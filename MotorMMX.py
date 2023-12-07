import os
import select

# motor0:ev3-ports:outA
# motor5:ev3-ports:in1:i2c3:M2
# motor3:ev3-ports:outD
# motor1:ev3-ports:outC
# motor4:ev3-ports:in1:i2c3:M1
# motor2:ev3-ports:outB

WAIT_RUNNING_TIMEOUT = 100

class SpeedValue:
    """
    The base class for the SpeedValue classes.
    Not meant to be used directly.
    Use SpeedNativeUnits, SpeedPercent, SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM
    """

    def __lt__(self, other):
        return self.to_native_units() < other.to_native_units()

    def __rmul__(self,other):
        return self.__mul__(other)

    def to_native_units(self):
        pass

    def __mul__(self, other):
        pass

class SpeedPercent(SpeedValue):
    """
    Speed as a percentage of the motor's maximum rated speed.
    Returns Tacho Counts via motor.max_speed
    """
    def __init__(self, percent):
        if -100 <= percent <= 100:
            self.percent = percent
        else:
            raise ValueError("Value must be between -100 and 100")

    def __str__(self):
        return str(self.percent) + '%'

    def __mul__(self,other):
        if isinstance(other, (float, int)):
            return SpeedPercent(self.percent * other)
        else:
            raise TypeError("Multiplier must be of int or float type.")

    def to_native_units(self, motor):
        return self.percent / 100 * motor.max_speed


class motorMMX:
    COMMAND_RESET = 'reset'
    COMMAND_RUN_DIRECT = 'run-direct'
    COMMAND_RUN_FOREVER = 'run-forever'
    COMMAND_RUN_TIMED = 'run-timed'
    COMMAND_RUN_TO_ABS_POS = 'run-to-abs-pos'
    COMMAND_RUN_TO_REL_POS = 'run-to-rel-pos'
    COMMAND_STOP = 'stop'
    ENCODER_POLARITY_INVERSED = 'inversed'
    ENCODER_POLARITY_NORMAL = 'normal'
    POLARITY_INVERSED = 'inversed'
    POLARITY_NORMAL = 'normal'
    STATE_HOLDING = 'holding'
    STATE_OVERLOADED = 'overloaded'
    STATE_RAMPING = 'ramping'
    STATE_RUNNING = 'running'
    STATE_STALLED = 'stalled'
    STOP_ACTION_BRAKE = 'brake'
    STOP_ACTION_COAST = 'coast'
    STOP_ACTION_HOLD = 'hold'

    _DIRECTORY_BASE = '/sys/class/tacho-motor'

    _PRE_OPENS = [
        ('command', 'w'),
        ('duty_cycle', 'r'),
        ('duty_cycle_sp', 'w+'),
        ('polarity', 'w+'),
        ('position', 'w+'),
        ('hold_pid/Kd', 'w+', 'position_d'),
        ('hold_pid/Ki', 'w+', 'position_i'),
        ('hold_pid/Kp', 'w+', 'position_p'),
        ('position_sp', 'w+'),
        ('ramp_down_sp', 'w+'),
        ('ramp_up_sp', 'w+'),
        ('speed', 'r'),
        ('speed_pid/Kd', 'w+', 'speed_d'),
        ('speed_pid/Ki', 'w+', 'speed_i'),
        ('speed_pid/Kp', 'w+', 'speed_p'),
        ('speed_sp', 'w+'),
        ('state', 'r'),
        ('stop_action', 'w+'),
        ('time_sp', 'w+')
    ]

    _PRE_READS = [
        ('address', str),
        ('commands', str),
        ('count_per_rot', int),
        ('count_per_m', int),
        ('full_travel_count', int),
        ('driver_name', str),
        ('max_speed', int),
        ('stop_actions', str)
    ]

    _DRIVER_NAME = None
    max_speed = 1000
    count_per_rot = 360

    speed_sp_table = [[], []]
    for i in range(0, 1561):
        speed_sp_table[0].append(str(i).encode())
        speed_sp_table[1].append(str(-i).encode())

    def __init__(self, port):

        self._fd = {}

        for item in os.listdir(self._DIRECTORY_BASE):
            rpn = open(self._DIRECTORY_BASE + "/" + item + "/address", "r")
            address = rpn.read()
            address = address.replace("\n", "")
            rpn.close()
            if address == port:
                self._port = port
                self._item = item
                self._directory = self._DIRECTORY_BASE + "/" + item + "/"
                print(item)
                print(address)
                print(self._DIRECTORY_BASE + "/" + item + "/")
                break

        self._pre_open()
        self._pre_read()

    def _pre_open(self):
        for pre_open in self._PRE_OPENS:
            f = open(self._directory + pre_open[0], pre_open[1])
            if (len(pre_open) > 2):
                self._fd[pre_open[2]] = f
            else:
                self._fd[pre_open[0]] = f
        # print(self._fd)

    def _pre_read(self):
        for pre_read in self._PRE_READS:
            try:
                with open(self._directory + pre_read[0], 'r') as f:
                    setattr(self, pre_read[0], pre_read[1](f.read()).replace("\n", ""))
            except:
                pass

    @property
    def command(self):
        raise Exception("command is a write-only property!")

    @command.setter
    def command(self, value):
        self._fd['command'].write(value.encode('ascii'))
        return 0

    @property
    def duty_cycle(self):
        return int(self._fd['duty_cycle'].read())

    @property
    def duty_cycle_sp(self):
        return int(self._fd['duty_cycle_sp'].read())

    @duty_cycle_sp.setter
    def duty_cycle_sp(self, value):
        self._fd['duty_cycle_sp'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def is_holding(self):
        return self.STATE_HOLDING in self.state

    @property
    def is_overloaded(self):
        return self.STATE_OVERLOADED in self.state

    @property
    def is_ramping(self):
        return self.STATE_RAMPING in self.state

    @property
    def is_running(self):
        return self.STATE_RUNNING in self.state

    @property
    def is_stalled(self):
        return self.STATE_STALLED in self.state

    @property
    def polarity(self):
        return str(self._fd['polarity'].read())

    @polarity.setter
    def polarity(self, value):
        self._fd['polarity'].write(value.encode('ascii'))
        return 0

    @property
    def position(self):
        return int(self._fd['position'].read())

    @position.setter
    def position(self, value):
        self._fd['position'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def position_d(self):
        return int(self._fd['position_d'].read())

    @position_d.setter
    def position_d(self, value):
        self._fd['position_d'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def position_i(self):
        return int(self._fd['position_i'].read())

    @position_i.setter
    def position_i(self, value):
        self._fd['position_i'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def position_p(self):
        return int(self._fd['position_p'].read())

    @position_p.setter
    def position_p(self, value):
        self._fd['position_p'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def position_sp(self):
        return int(self._fd['position_sp'].read())

    @position_sp.setter
    def position_sp(self, value):
        self._fd['position_sp'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def ramp_down_sp(self):
        return int(self._fd['ramp_down_sp'].read())

    @ramp_down_sp.setter
    def ramp_down_sp(self, value):
        self._fd['ramp_down_sp'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def ramp_up_sp(self):
        return int(self._fd['ramp_up_sp'].read())

    @ramp_up_sp.setter
    def ramp_up_sp(self, value):
        self._fd['ramp_up_sp'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def speed(self):
        return int(self._fd['speed'].read())

    @property
    def speed_d(self):
        return int(self._fd['speed_d'].read())

    @speed_d.setter
    def speed_d(self, value):
        self._fd['speed_d'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def speed_i(self):
        return int(self._fd['speed_i'].read())

    @speed_i.setter
    def speed_i(self, value):
        self._fd['speed_i'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def speed_p(self):
        return int(self._fd['speed_p'].read())

    @speed_p.setter
    def speed_p(self, value):
        self._fd['speed_p'].write(str(int(value)).encode('ascii'))
        return 0

    @property
    def speed_sp(self):
        return int(self._fd['speed_sp'].read())

    @speed_sp.setter
    def speed_sp(self, value):
        if value > 0:
            self._fd['speed_sp'].write(self.speed_sp_table[0][value])
        else:
            self._fd['speed_sp'].write(self.speed_sp_table[1][-value])
        return 0

    @property
    def state(self):
        return str(self._fd['state'].read())

    @property
    def stop_action(self):
        """
        Reading returns the current stop action.
        Use stop_actions for the list of possible values.
        """
        return str(self._fd['stop_action'].read())

    @stop_action.setter
    def stop_action(self, value):
        self._fd['stop_action'].write(value.encode('ascii'))
        return 0

    @property
    def time_sp(self):
        return int(self._fd['time_sp'].read())

    @time_sp.setter
    def time_sp(self, value):
        self._fd['time_sp'].write(str(int(value)).encode('ascii'))
        return 0

    def reset(self, **kwargs):
        """
        Resets the motor the default value. It will also stop the motor.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('reset\n')

    def run_direct(self, **kwargs):
        """
        Run the motor at the duty cycle specified by duty_cycle_sp.
        Unlike other run commands, changing duty_cycle_sp
        while running will take effect immediately.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('run-direct\n')

    def run_forever(self, **kwargs):
        """
        Run the motor until another command is sent.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('run-forever\n')

    def run_timed(self, **kwargs):
        """
        Run for the amount of time specified in time_sp.
        Then, stop the motor as specified by stop_action.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('run-timed\n')

    def run_to_abs_pos(self, **kwargs):
        """
        Run to the absolute position as specified by position_sp.
        Then, stop the motor as specified by stop_action.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('run-to-abs-pos\n')

    def run_to_rel_pos(self, **kwargs):
        """
        Run to the relative position as specified by position_sp.
        New position will be current position + position_sp
        When the new position is reached, the motor will stop, as specified
        by stop_action.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('run-to-rel-pos\n')

    def stop(self, **kwargs):
        """
        Stop any of the run commands before they are complete using the
        action specified by stop_action.
        """
        for k in kwargs:
            setattr(self, k, kwargs[k])
        self._fd['command'].write('stop\n')

    def wait(self, cond, timeout=None):
        """
        Blocks until ``cond(self.state)`` is ``True``.  The condition is
        checked when there is an I/O event related to the ``state`` attribute.
        Exits early when ``timeout`` (in milliseconds) is reached.

        Returns ``True`` if the condition is met, and ``False`` if the timeout
        is reached.

        Valid flags for state attribute: running, ramping, holding,
        overloaded and stalled
        """
        poll = select.poll()
        poll.register(self._fd['state'], select.POLLIN)

        while True:
            event = poll.poll(timeout)

            if len(event) == 0:
                return False

            if cond(self.state):
                return True

    def wait_until(self, s, timeout=None):
        """
        Blocks until ``s`` is in ``self.state``.  The condition is checked when
        there is an I/O event related to the ``state`` attribute.  Exits early
        when ``timeout`` (in milliseconds) is reached.

        Returns ``True`` if the condition is met, and ``False`` if the timeout
        is reached.

        Example::
            m.wait_until('stalled')
        """
        return self.wait(lambda state: s in state, timeout)

    def wait_until_not_moving(self, timeout=None):
        """
        Blocks until one of the following conditions are met:
        - ``running`` is not in ``self.state``
        - ``stalled`` is in ``self.state``
        - ``holding`` is in ``self.state``
        The condition is checked when there is an I/O event related to
        the ``state`` attribute.  Exits early when ``timeout`` (in
        milliseconds) is reached.

        Returns ``True`` if the condition is met, and ``False`` if the timeout
        is reached.

        Example::
            m.wait_until_not_moving()
        """
        return self.wait(lambda state: self.STATE_RUNNING not in state or self.STATE_STALLED in state, timeout)

    def wait_while(self, s, timeout=None):
        """
        Blocks until ``s`` is not in ``self.state``.  The condition is checked
        when there is an I/O event related to the ``state`` attribute.  Exits
        early when ``timeout`` (in milliseconds) is reached.

        Returns ``True`` if the condition is met, and ``False`` if the timeout
        is reached.

        Example::

            m.wait_while('running')
        """
        return self.wait(lambda state: s not in state, timeout)

    def _set_rel_position_degrees_and_speed_sp(self, degrees, speed):
        degrees = degrees if speed >= 0 else -degrees
        speed = abs(speed)

        position_delta = int(round((degrees * self.count_per_rot)/360))
        speed_sp = int(round(speed))

        self.position_sp = position_delta
        self.speed_sp = speed_sp

    def on_for_rotations(self, speed, rotations, brake=True, block=True):
        """
        Rotate the motor at ``speed`` for ``rotations``

        ``speed`` can be a percentage or a :class:`ev3dev2.motor.SpeedValue`
        object, enabling use of other units.
        """
        if not isinstance(speed, SpeedValue):
            if -100 <= speed <= 100:
                speed = SpeedPercent(speed)
                speed_sp = speed.to_native_units(self)
            else:
                raise Exception("Invalid Speed Percentage. Speed must be between -100 and 100)")
        else:
            speed_sp = int(round(speed.to_native_units(self)))

        self._set_rel_position_degrees_and_speed_sp(rotations*360, speed_sp)

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.run_to_rel_pos()

        if block:
            self.wait_until('running', timeout=WAIT_RUNNING_TIMEOUT)
            self.wait_until_not_moving()

    def on_for_degrees(self, speed, degrees, brake=True, block=True):
        """
        Rotate the motor at ``speed`` for ``degrees``

        ``speed`` can be a percentage or a :class:`ev3dev2.motor.SpeedValue`
        object, enabling use of other units.
        """
        if not isinstance(speed, SpeedValue):
            if -100 <= speed <= 100:
                speed = SpeedPercent(speed)
                speed_sp = speed.to_native_units(self)
            else:
                raise Exception("Invalid Speed Percentage. Speed must be between -100 and 100)")
        else:
            speed_sp = int(round(speed.to_native_units(self)))

        self._set_rel_position_degrees_and_speed_sp(degrees, speed_sp)

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.run_to_rel_pos()

        if block:
            self.wait_until('running', timeout=WAIT_RUNNING_TIMEOUT)
            self.wait_until_not_moving()

    def on_to_position(self, speed, position, brake=True, block=True):
        """
        Rotate the motor at ``speed`` to ``position``

        ``speed`` can be a percentage or a :class:`ev3dev2.motor.SpeedValue`
        object, enabling use of other units.
        """
        if not isinstance(speed, SpeedValue):
            if -100 <= speed <= 100:
                speed = SpeedPercent(speed)
                speed_sp = speed.to_native_units(self)
            else:
                raise Exception("Invalid Speed Percentage. Speed must be between -100 and 100)")
        else:
            speed_sp = int(round(speed.to_native_units(self)))

        self.speed_sp = int(round(speed_sp))
        self.position_sp = position

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.run_to_abs_pos()

        if block:
            self.wait_until('running', timeout=WAIT_RUNNING_TIMEOUT)
            self.wait_until_not_moving()

    def on_for_seconds(self, speed, seconds, brake=True, block=True):
        """
        Rotate the motor at ``speed`` for ``seconds``

        ``speed`` can be a percentage or a :class:`ev3dev2.motor.SpeedValue`
        object, enabling use of other units.
        """
        if seconds < 0:
            raise ValueError("Seconds is negative.")

        if not isinstance(speed, SpeedValue):
            if -100 <= speed <= 100:
                speed = SpeedPercent(speed)
                speed_sp = speed.to_native_units(self)
            else:
                raise Exception("Invalid Speed Percentage. Speed must be between -100 and 100)")
        else:
            speed_sp = int(round(speed.to_native_units(self)))

        self.speed_sp = int(round(speed_sp))
        self.time_sp = int(seconds * 1000)

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.run_timed()

        if block:
            self.wait_until('running', timeout=WAIT_RUNNING_TIMEOUT)
            self.wait_until_not_moving()

    def on(self, speed, brake=True, block=False):
        if not isinstance(speed, SpeedValue):
            if -100 <= speed <= 100:
                speed = SpeedPercent(speed)
                speed_sp = speed.to_native_units(self)
            else:
                raise Exception("Invalid Speed Percentage. Speed must be between -100 and 100)")
        else:
            speed_sp = int(round(speed.to_native_units(self)))

        self.speed_sp = int(round(speed_sp))

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.run_forever()

        if block:
            self.wait_until('running', timeout=WAIT_RUNNING_TIMEOUT)
            self.wait_until_not_moving()

    def off(self, brake=True):

        if brake:
            self.stop_action = self.STOP_ACTION_HOLD
        else:
            self.stop_action = self.STOP_ACTION_COAST

        self.stop()
