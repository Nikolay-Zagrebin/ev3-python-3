#!/usr/bin/python3

import ev3dev.ev3 as ev3

# variable names and values

# here are examples of values
1
1.1
"Hello"

# but we can also use variables to store values
x      # if a variable is not defined, we cannot use it
x = 1  # assign a number to the variable x
       # after assignment, the variable x has value 1

# guess what will happen when we run the following two
# commands?
ev3.Sound.speak(x).wait()
ev3.Sound.speak('x').wait()

# you can assign to new variables using old ones
y = x
ev3.Sound.speak(y).wait()

x = 2
ev3.Sound.speak(y).wait()
ev3.Sound.speak(x).wait()

## nesting expression
ev3.Sound.speak(x+y).wait()  # because x+y is an expression,
                             # it will be evaluated first,
                             # then the value will be passed to
                             # the speak function

z = 2*x-y
ev3.Sound.speak(z-y/x).wait()
