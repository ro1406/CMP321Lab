# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:22:15 2022

@author: rohan
"""

'''
a)	Create a Primes iterator class that will give prime numbers infinitely.
1.	Write an initializer that takes a starting number, give a default value of 2.
2.	Write the __iter__ method that returns the object itself.
3.	Write the __next__  method that produces the next prime number.
'''

from Q1 import isPrime

class Primes:
    def __init__(self,s=2):
        self.curr=s
        
    def __iter__(self):
        return self
    
    def __next__(self):
        n=self.curr+1
        while not isPrime(n):
            n+=1
        self.curr=n
        return n

'''
b)	Test the class developed in ex2 part(a) 
1.	Write a for loop to print the first 20 primes.
2.	Use list comprehension to create a list of the next 20 primes.
3.	Use islice() to create a list of the first 20 primes larger than 1 million.

'''
#1:
primes=Primes()
print("First 20 primes with a for loop:")
for x in range(20):
    print(next(primes))
 
print('-'*95)

#2:
primes=Primes()
twentyPrimes=[next(primes) for x in range(20)]
print("First 20 primes using list comprehension:")
print(twentyPrimes)
print('-'*95)

#3:
from itertools import islice
primes=Primes(1_000_000)
print("First 20 primes over 1 million using islice:")
print(list(islice(primes,0,20)))
