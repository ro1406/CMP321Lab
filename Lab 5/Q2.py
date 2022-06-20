# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:38:03 2022

@author: keshav
"""

from functools import reduce

def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i + arr[i:].index(reduce(lambda x,y : x if x < y else y, arr[i::]))
        if(minIndex != i):
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

arr = [-3, 5, 2, 8, 2, 9, 0, -7]
print("Unsorted Array: ",arr)	
selectionSort(arr)
print("Sorted Array: ", arr)
