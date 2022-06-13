# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:07:13 2022

@author: rohan
"""
def enum(arr,start=0,step=1):
    return [(step*i+start,arr[i]) for i in range(len(arr))  ]

print(enum( ['A', 'B', 'C'] ))
print(enum( ['A', 'B', 'C'], 5 ))
print(enum( ['A', 'B', 'C'], 4, 2 ))