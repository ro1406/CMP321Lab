# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:07:06 2022

@author: rohan
"""

from functools import reduce
'''
Part(a):
1.	Define a list that represents a list of temperatures in Fahrenheit. 
2.	Define a function that converts a temperature from Fahrenheit to Celsius (C=F–32 x 5/9)
3.	Use map function to generate a list temperatures in Celsius, then print it.

'''
farenheit=[i for i in range(1,100+1,10)]

def F2C(F):
    return (F-32) * 5./9.
print("Temperatures in Farenheit:")
print(farenheit)
print()
print("Temperatures in Celsius using map:")
celsius=list(map(F2C,farenheit))
print(celsius)

print('-'*90)
'''
Part(b):
4.	Perform step 3 using lambda expression

5.	Using the filter function and lambda expression, return a list of negative temperatures (based on list generated in part a, step 3).

'''

print("Temperatures in Celsius using lambda expression:")
print(list(map(lambda F:(F-32) * 5./9.,farenheit)))

print('-'*90)

print("List of negative temperatures:")
print( list(filter(lambda x:x<0,celsius)) )

print('-'*90)
'''
Part(c):
6.	Perform step 3 using list comprehension (i.e., do NOT use map, function or lambda)

7.	Perform step 5 using list comprehension

'''
print("Generate Celsius with list comprehrension:")
print([(F-32)*5./9. for F in farenheit])

print('-'*90)

print("Negative numbers using list comprehension:")
print([x for x in celsius if x<0])

print('-'*90)
'''
Part(d):
8.	Apply reduce to calculate the average of temperatures (in Celsius) 

9.	Using reduce, calculate the standard deviation of the temperatures as per the formula 
Use a lambda expression to calculate (xi – avg)2 , where avg is the average in step 8. 

'''
print("Average of temperatures using Reduce:")
avg=reduce(lambda x,y:x+y,celsius) / len(celsius)
print(avg)

print('-'*90)

print("Std div of temperatures using Reduce + Lambda Expression:")
print( ( ( reduce(lambda x,y: x+y, map(lambda x:(x-avg)**2,celsius ) ) ) / (len(celsius)-1) )**0.5 )

print('-'*90)
