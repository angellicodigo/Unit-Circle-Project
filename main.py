from numpy import *

print("Please use () for trig. functions, use x for theta, use sqrt() to square root, and don't use LaTeX syntax.")
lhs_text = input("Enter the equation: ")
# rhs = .safe_eval(str(eval(iut('Enter what the equation equals to: ')))) # somewhat evaluating iut safely
rhs_text = input("Enter what the equation equals to: ")
rhs = eval(rhs_text) 
lhs = lhs_text.lower().replace(')', '').split('(') # i.e might get something like ['cos', 'x']

inverse = 0 # Getting the trig inverse of the rhs
if (lhs[0] == 'sin'):
  inverse = arcsin(rhs)
elif (lhs[0] == 'cos'):
  inverse = arccos(rhs)
elif (lhs[0] == 'tan'):
  inverse = arctan(rhs)
elif (lhs[0] == 'csc'): # csc^-1(x) = sin^-1(x^-1)
  inverse = arcsin(rhs ** -1)
elif (lhs[0] == 'sec'): # sec^-1(x) = cos^-1(x^-1)
  inverse = arccos(rhs ** -1)
elif (lhs[0] == 'cot'): # cot^-1(x) = tan^-1(x^-1)
  inverse = arctan(rhs ** -1)

half = 1 # default value
double = 1 # default value
# Isolating the expressions/numbers around the x variable
expression = lhs[1].replace('x', '').split('/') # Spliting in case of given iut like 'x/2'

if (len(expression) == 2): # Works when iut is like 'x/2' or '2x/3'
  if (expression[0] == ''): # In case only a half angle is given
    half = int(expression[1])
  else: # For both half and double angle
    half = int(expression[0])
    double = int(expression[1])
elif (expression[0] != ''): # Only a double angle is given
  double = int(expression[0])

solution = half * inverse / double # equation in the text

print(f"First solution in radians: {solution}")

if (solution < 0): # If output is negative, convert it to positive
  # Convert to positive to find multpiles of the given output
  solution = abs(solution) # it isn't the actually solution, just the solution for positive rhs

multiples = 1 # Multipying the first/solved solution to get the other solution, cant skip first iteration bc negative
solutions = [] # List of solutions to the equation
# reference_angle = (double * solution) / half # The normal angle for the value without doubling or halving it

n = 1 # nth power
if (lhs[0] == 'csc' or lhs[0] == 'sec' or lhs[0] == 'cot'): 
  n = -1 # using an idea like cot(x) = tan(x)^-1 

if (lhs[0] == 'sin' or lhs[0] == 'csc'): 
  while multiples * solution < 2 * pi: # [0, 2pi)
    # sin(multiples of x) == sin(reference angle)
    if round(sin(double * multiples * solution / half) ** n, 10) == round(rhs, 10): # rounding both to avoid problems
      solutions.append(multiples * solution)
    multiples += 1

elif (lhs[0] == 'cos' or lhs[0] == 'sec'):
  while multiples * solution < 2 * pi: # [0, 2pi]
    # cos(multiples of x) == cos(reference angle)
    if round(cos(double * multiples * solution / half) ** n, 10) == round(rhs, 10): # rounding both to avoid problems 
      solutions.append(multiples * solution)
    multiples += 1

elif (lhs[0] == 'tan' or lhs[0] == 'cot'):
  while multiples * solution < 2 * pi: # [0, 2pi)
    # tan(multiples of x) == tan(reference angle)
    if round(tan(double * multiples * solution / half) ** n, 10)  == round(rhs, 10): # rounding both to avoid problems
      solutions.append(multiples * solution)
    multiples += 1

print(f"Solutions: {solutions}")

import matplotlib.pyplot as plt
from random import random

plt.axes(projection = 'polar') # using polar graph
plt.style.use('default')
plt.xticks([0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, 
            pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6]) # ticks of unit circle
plt.yticks([]) 
plt.title(f'Unit Circle of {lhs_text} = {rhs_text}', pad = 15)
plt.grid(False)
plt.plot([0, pi], [1, 1], 'black', alpha = 0.725) # x-axis
plt.plot([pi/2, 3*pi/2], [1, 1], 'black', alpha = 0.725) # y-axis
degrees =  rad2deg(solutions) # list of the radians converting to degrees

for index in range(len(solutions)):
  r = random()
  b = random()
  g = random()
  color = (r, g, b) # randomly generate a color
  plt.polar([0, solutions[index]], [0, 1], color = color) # plot line with radius of 1
  theta = arange(0, solutions[index], 0.01) # Creating array of angles at evenly spaced intervals
  # using logistic growth equation for the angle to not go beyond radius of 1
  radius = 1 / (1 + len(solutions) * exp(-0.5 * index)) # len(solutions) to scale the initial value 
  r = linspace(radius, radius, len(theta)) # array of the same number
  plt.polar(theta, r, color = color, label = f'{round(degrees[index], 1)}') # plot angle with changing radius

plt.legend(loc = (1.1, 0.25), shadow = True)
plt.show()