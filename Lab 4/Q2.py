# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:33:00 2022

@author: rohan
"""

class Employee:
    def __init__(self,ID,name,surname,rank):
        self.id=ID
        self.name=name
        self.surname=surname
        self.rank=rank

    def __str__(self):
            s="\nID = " +repr(self.id)
            s += "  name = "+self.name
            s +="  Surname = "+self.surname
            s += "  Rank = " +repr(self.rank)
            return s;
    
    
    def __lt__(self,other):
         return (self.id < other.id)
    def __gt__(self,other):
         return (self.id > other.id)

def sort(values, comp=Employee.__gt__):
    for i in range(1, len(values)):
        for j in range(0, len(values)-1):
            if (comp(values[j],values[j+1])):#if(values[j] > values[j+1]):
                values[j], values[j+1] = values[j+1], values[j];

    return values

e1=Employee(10456,"AlKhan", "Ahmed",  3)
e2=Employee(10456,"AlKhan", "Ahmed",  3)
e3=Employee(23670, "Mariam", "AlSaleh", 1)
e4=Employee(11673, "Adbulla", "Malek", 2)
e5=Employee(40074, "Nour", "AlAli", 5)

lst=[e1,e2,e3,e4,e5]

'''
You are provided with an Employee class that has four attributes: ID, name, surname, rank (rank is a number between 1 to 5). 
__init__ and __str__ , as well as all comparison operators <, > i.e., __lt_ and __gt__ (that should compare IDs) are provided. 
Given Sort function is from Lab1.

Do the following,
Print all employees, 
•	Sorted by ID
•	Sorted by name 
•	Sorted by rank then by ID when the rank is the same. 

Note that for ID the default > operator used by sort should suffice. No lambda is required. However, for others pass a lambda that compares the relevant fields is required.

'''
print("By ID:")
res=sort(lst)
for x in res:print(x,end=" ")
print('-'*90)

print("By Name:")
res=sort(lst,lambda x,y: x.name>y.name)
for x in res:print(x,end=" ")

print('-'*90)
print("By Rank then by ID:")
res=sort(lst,lambda x,y: x.id>y.id if x.rank==y.rank else x.rank>y.rank)
for x in res:print(x,end=" ")