# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:36:38 2022

@author: Keshav Ramesh
"""

values = [50, 12, 27, 33, 61, 49, 28]

for _ in values:
    for j in range (len(values)-1):
        if values[j]>values[j+1]:
            values[j], values[j+1] = values [j+1], values[j]

print("Array after bubble sort: ", end = ""); print(values)
