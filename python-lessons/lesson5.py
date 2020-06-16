#!/usr/bin/python3

# Why do we need to use functions?
# 1. Because you can pass different parameters to the same function
# 2. Because it represent a unit of computation, which can be reused
# 3. Functions can be reused by other people

# examples of functions

def add(x,y):  #here x and y are parameters of the function
  # x and y can be used in the body of the function
  return(x+y)

add(3,5)

def sq(x):
  return(x*x)

sq(4)
sq(29)

def area_of_triangle(b,h):
  return(b*h/2)

area_of_triangle(300,467)
area_of_triangle(1,2)

## Fibonacci 
## can you write a function that can give you the
## n-th Fibonacci number?

def fib(a):
  if a == 1:
    return(1)
  if a == 2:
    return(1)
  else:
    return(fib(a-1)+fib(a-2))

fib(1)
fib(2)
fib(3)
fib(10)
  
for a in range(1,20):
 fib(a)
