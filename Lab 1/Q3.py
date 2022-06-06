# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:12:44 2022

@author: rohan
"""

'''
a.	Given a list of full names, print acronyms for each by combining the first letter of the first name and the last name (ignoring middle names, if any). Example:
    nameList = ["Abdulla mhd zayed", "rashid asif", "john elton rowan smith", "Ali Rami"] 
    printed acronyms:  AZ, RA, JS, AR.

'''
nameList=["Abdulla mhd zayed", "rashid asif", "john elton rowan smith", "Ali Rami"] 

print(*[fullName.split()[0][0].upper()+ fullName.split()[-1][0].upper() for fullName in nameList])


'''

b.	Given a string, such as "Welcome to UAE. uae is awesome, right?", find all occurrences of "UAE" in that string (ignoring case).

'''
s="Welcome to UAE. uae is awesome, right?"

print(s.lower().count('uae')) #.lower to ignore the case