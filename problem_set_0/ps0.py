# Problem Set 0 - Introduction to Computer Science and Programming in Python
# produce number 'x' raised to the power of number 'y'
# produce log (base 2) of 'x'

import numpy as np

x = input('Enter number x:')
y = input('Enter number y:')

power = int(x)**int(y)

print('X**y = ' + str(power))

log = np.log2(int(x))

print ('log(x) = ' + str(log))
