# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:17:17 2022

@author: rohan
"""
#Q1:
import math
def isPrime(n,div=2):
    if div>math.sqrt(n):
        return True
    if n%div==0:
        return False
    return isPrime(n,div+1)

for x in range(2,30+1): print(f'{x}: {isPrime(x)}')