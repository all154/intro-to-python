# Problem Set 0 - Introduction to Computer Science and Programming in Python
# produce number 'x' raised to the power of number 'y'

# receive inputs
x = input('Enter number x:')
y = input('Enter number y:')

# calculating
pwr=int(x)**int(y)

# returning result
print('X**y = ' + str(pwr))

# produce log (base 2) of 'x'

# importing numpy library to use log function
import numpy as np

# returning log (base 2) of 'x'
print ('log(x) = ' + str(np.log2(int(x))))