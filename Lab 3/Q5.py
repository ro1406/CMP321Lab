# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:46:36 2022

@author: keshav
"""
#Q5 part (a)

from math import sqrt

def apply_all(func, lst):
    return list((func(i) for i in lst))

l1 = [4, 9, 16, 25]
print(apply_all(sqrt, l1))

#(b)

print(apply_all(lambda lst:str(lst).isdigit(), ["1234", "hellow","class23"]))