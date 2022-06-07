# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:33:14 2022

@author: Keshav Ramesh
"""

text = "The best programs are written so that computing machines can perform them quickly and so that human beings can understand them clearly. A programmer is ideally an essayist who works with traditional aesthetic and literary forms as well as mathematical concepts, to communicate the way that an algorithm works and to convince a reader that the results will be correct..."
text = text.lower()
letters = {}
for i in text:
    if 'a' <= i <= 'z' :
        if i in letters.keys():
            letters[i] += 1
        else:
            letters[i] = 1
            
#Could just print(letters), but this is just to print nicely:
for key in sorted(letters.keys()):
    print(f'{key} appears {letters[key]} times')
