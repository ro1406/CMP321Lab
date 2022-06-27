# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:14:08 2022

@author: keshav
"""

"""
Write a Python script that uses a regular expression to check if a string represents a valid phone number, or not, as per the following specifications (grammar rules). Examples of valid phone numbers include: "(971) 50-5672722", "971-55-6713432", "971-6-5150000, and "056-8887272". 

(1) A phone number is either of:
– A country code in parentheses, followed by a space character, and a full number;
– A country code, followed by a dash character ('–'), and full number;
– A zero ('0'), followed by full number.

(2) A country code consists of three digits.

(3) A full number is a mobile code or an area code, followed by a dash ('–'), and a number.

(4) A mobile code is either 50 or 55 or 56.  

(5) An area code is any of 2, 3, 4, 6, 7, or 9.

(6) A number consists of seven digits.

(7) A digit is any from 0 to 9.

"""


import re 

def checkPhoneNo(num):
    if re.fullmatch(r"((\(\d{3}\) )|(\d{3}-)|0)(50|55|56|2-4|6|7|9)-\d{7}", num):
        print(num, "is a valid phone number")
    else: 
        print(num, "is an invalid phone number")

lst = ["(971) 50-5672722", "971-55-6713432", "971-6-5150000" , "056-8887272" ]

for item in lst:
    checkPhoneNo(item)