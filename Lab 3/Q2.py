# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:02:48 2022

@author: rohan
"""

def fun(names,locations,majors):
    return [f'{name} from {maj} lives in {loc}' for name,maj,loc in zip(names,majors,locations)]

print(fun( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"], 
    ["COE", "CMP", "ELE"] ))
