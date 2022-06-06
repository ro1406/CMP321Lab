# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:46:15 2022

@author: Keshav Ramesh
"""

#Part (a)
string = "Welcome to Python"
print(string[5:10])
print(string[4:]) #5th char onwards (AFTER 4th char)
print(string[-5:])
print(string == string[::-1])

#Part (b)

places = ["Cairo", "Egypt", "Baghdad", "Iraq", "Delhi", "India", "Tehran", "Iran", "Riyadh", "Saudi Arabia", "Ankara", "Turkey"]
print(places[::2]) #Even indicies
print(places[::-2]) #Odd indicies backwards
places[places.index('Delhi')]="Muscat"
places[places.index('India')]="Oman"
print(places)

