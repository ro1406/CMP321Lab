# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:42:39 2022

@author: rohan
"""

'''
a)	Write a prime number generator, using the prime function developed in ex1. 
By default it should generate (infinitely) all primes. 
If given a value as argument, it should generate (infinitely) all primes larger than this value.  

'''
#part (a)
from Q1 import isPrime

def generatePrimes(x=2):
    while True:
        if isPrime(x):
            yield x
        x+=1

'''
b)	Test the class developed in ex3 part(a) 
1.	Write a for loop to print the first 20 primes.
2.	Use list comprehension to create a list of the next 20 primes.
3.	Use islice() to create a list of the first 20 primes larger than 1 million.
4.	Use a generator expression to create an iterator that would produce the first 100 primes larger than 1 million, then use a for loop and this iterator to print the values. 
5.	Use the above iterator to create a list of the first 100 primes larger than 1 million for which the last two digits are identical.

'''

#part(b)
#1:

print("First 20 primes with a for loop:")
gen=generatePrimes()
for x in range(20):
    print(next(gen), end = " ")
 
print('-'*95)

#2:
twentyPrimes=[next(gen) for x in range(20)]
print("First 20 primes using list comprehension:")
print(twentyPrimes)
print('-'*95)

#3:
from itertools import islice
print("First 20 primes over 1 million using islice:")
print(list(islice(generatePrimes(1_000_000),0,20)))
print('-'*95)

#4:

gen=generatePrimes(1_000_000)
print("First 100 primes past a million: ")
for x in range(100):
    print(next(gen), end = " ")
 
print('-'*95)

#5:
gen=generatePrimes(1_000_000)
print("The list of primes after 1 million with identical last digits are: ")
print([x for x in islice(generatePrimes(1_000_000),0,100) if str(x)[-1]==str(x)[-2]])