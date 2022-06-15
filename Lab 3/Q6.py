# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:33:16 2022

@author: keshav
"""

#Part (a)

from math import factorial as fact

def t(n):
    
    def f(k):
        return fact(n)//(fact(k)*fact(n-k))
    return f

print(" 10 C 3 (computed using nested functions) is" , t(10)(3))

#Part (b)

def C(n):
    return lambda k: fact(n)//(fact(k)*fact(n-k))

fun = C(10)

print(" 10 C 3 (computed using lambda expressions) is" , fun(3))