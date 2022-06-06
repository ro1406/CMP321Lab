# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:40:36 2022

@author: rohan
"""

'''
a.	Display sin and cos values of n in the range 1 to 10 in a tabular format as given below with 5 decimals. Use formatting method from string class.

 1         0.84147         0.54030
 2         0.90930        -0.41615
 3         0.14112        -0.98999
 4        -0.75680        -0.65364
 5        -0.95892         0.28366
 6        -0.27942         0.96017
 7         0.65699         0.75390
 8         0.98936        -0.14550
 9         0.41212        -0.91113
10       -0.54402        -0.83907

'''

import math

for i in range(1,10+1): print('{:2d} {:10.5f} {:10.5f}'.format(i, math.sin(i), math.cos(i)))

print("-"*95)
'''
b.	Using F-String format print n and 2**n as given below. 
n is in the range 0 to 160 increment by 8. n is right aligned, and 2**n is center aligned. 

'''
for n in range(0,160+1,8): print(f'{n:3d} {2**n:^49}')
    