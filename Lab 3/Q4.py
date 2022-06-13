# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:13:05 2022

@author: rohan
"""

#part a)
def member(x,arr):
    if len(arr)==0:
        return False
    if x==arr[0]:
        return True
    return member(x,arr[1:])


print(member( 2, [1, 3, 5] ))
print(member( 4, [1, 2, 3, 4, 5] ))


#part b)

def indexOf(x,arr,acc=0):
    if len(arr)==0:
        return -1
    if x==arr[0]:
        return acc
    return indexOf(x,arr[1:],acc+1)

print(indexOf(  2, [1, 3, 5] ))	
print(indexOf( 4, [1, 2, 3, 4, 5] ))