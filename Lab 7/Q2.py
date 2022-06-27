# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:12:41 2022

@author: keshav
"""

"""
Write a Python script that uses a regular expression to check if a given string represents a valid assignment expression, or not, as defined by the following specifications (grammar rules). Examples are included hereafter.

(1) An assignment expression is:
– An identifier, followed by the equal sign ('='), followed by either of an identifier or a number 
– optionally followed by one or more of : an operator followed by either an identifier or a number.

(2) An identifier is a letter, optionally followed by one or more of:  a letter or a digit.

(3) A number may optionally start with either the plus sign ('+') or minus sign ('–'). It consists of one or more digits, optionally followed by: a decimal point ('.') and one or more digits.

(4) An operator is either of the symbols for addition ('+'), subtraction ('–'), multiplication ('*'), division ('/'), or modulus ('%').

(5) A letter is any character from the small or uppercase alphabets: 'a-z' or 'A-Z'.

(6) A digit is any from 0 to 9.

"""

import re

def checkExpression(expression):
    if re.fullmatch(r"([a-zA-Z]+[0-9]*[a-zA-Z]* = [+-]?\w+(\.[0-9])*( *[+\-*/%] [+-]?\w+(\.[0-9])*)*)",expression):
        return True
    return False
    

lst = ["x = y", "y = y * z", "z = a + b - 1 / c", "p = 3.1415 * d", "x = y *","y = y z","z = + b – 1 /c","3 = p * d",'x = -3 + y','x = y / -3'] #test cases for checking expression

for item in lst:
    print(item,':',checkExpression(item))
