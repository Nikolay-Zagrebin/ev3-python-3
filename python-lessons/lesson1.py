#!/usr/bin/python3

import ev3dev.ev3 as ev3

# this is a comment and will not be run

# examples of numbers
1   # this is an integer
1.1 # this is a floating point number
    # however, python does not support fractions

# examples of strings
"Hello"
"hi","my","lol"
ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
ev3.Sound.speak('Albert is awesome and cool'       ).wait()
ev3.Sound.speak('1+1+2+4+8+16+32+64+128+256 equals 512').wait()

# example of expressions
1.1+2.3
1.3*2.6+3.4/4.98+3.65-76.90875648+100
((1.2+3.980764532193)/70.7089+4.78)/12.9086745132+125.90
