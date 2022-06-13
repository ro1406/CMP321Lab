# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:46:36 2022

@author: keshav
"""
#Q5 part (a)

from math import sqrt

def apply_all(func, lst):
    return [func(i) for i in lst]

l1 = [4, 9, 16, 25]
print(apply_all(sqrt, l1))

#(b)
li=["1234", "hellow","class23"]
ans=apply_all(lambda lst:str(lst).isdigit(), li)
print("The elements that contain only numbers are:")
for string,x in zip(li,ans):
    if x:
        print(string)