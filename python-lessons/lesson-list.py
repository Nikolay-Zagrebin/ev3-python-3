#!/usr/bin/python3

import ev3dev.ev3 as ev3

# a list is a data structure that hold more than one values

# create a list use a pair of brackets, and separate each
# value with a comma

# a list of numbers:
[1,2,3]

# a list of strings
['the' ,'this','that']

['+', '-', '*', '/']

# We can write out the expressions
1+1
1-1
1*1
1/1

# operations between two strings
'1+1'
'1' + '+' + '1'
'Hi!' + ' Al!'

# or we can use a for loop
for j in ['+', '-', '*', '/']:
  print(j)


operators = ['+', '-', '*', '/']

operators

# is this expression or statement
print(1)

for j in operators:
  print(j)

# block statements (such as for and def)
for x in range(0,2):
print("HAHA")

for x in range(0,2):
  print("HAHA")

for x in range(0,2):
  print("HAHA")
  for y in range(0,2):
    print("WELL WELL")

for x in range(0,2):
  print("HAHA")

print("WELL WELL")



## task: print out the expressions containing '1 op 2', where op is an operator 
op = operators

for j in operators:
  print ('1' + j + '2')

for j in operators:
  expr = '1' + j + '2'
  print(expr)

for j in operators:
  expr = '1' + j + '2'
  print(eval(expr))

for j in operators:
  expr = '1' + j + '2'
  print(expr + '=', end='')
  print(eval(expr))

# print 1/(2**0) + 1/(2**1) + 1/(2**2) + 1/(2**3) + ...
result = 0.0
for j in range(1,100):
  result = result + 1/(2**j)

print(result)
