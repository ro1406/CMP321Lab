# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:46:15 2022

@author: Keshav Ramesh
"""

#Part (a)

string = "Welcome to Python"
print(string[5:10])
print(string[4:])
print(string[-5:])
print(string[:] == string[::-1])

#Part (b)

places = ["Cairo", "Egypt", "Baghdad", "Iraq", "Delhi", "India", "Tehran", "Iran", "Riyadh", "Saudi Arabia", "Ankara", "Turkey"]
print(places[1::2])
print(places[::-2])