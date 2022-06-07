# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:11:50 2022

@author: Keshav Ramesh
"""

points = [(1,2,3) , (4,5,6) , (7,8,9) , (10, 11, 12), (13,14,15)]
points.pop()
points.insert(-2, (17,18,19))
print ("{:>4} {:>4} {:>4}".format('X', 'Y', 'Z'))
for i in points:
    print ("{:>4} {:>4} {:>4}".format(str(i[0]), str(i[1]), str(i[2])))