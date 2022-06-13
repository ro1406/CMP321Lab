# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:17:28 2022

@author: rohan
"""

#part a)

def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

print([fib(i) for i in range(11)])

#part b)

def fibAcc(n):
    def fibAccPrivate(n,prev=0,acc=1):
        if n<=0:
            return acc
        return fibAccPrivate(n-1,acc,prev+acc)
    return fibAccPrivate(n)

print([fibAcc(i) for i in range(11)])
