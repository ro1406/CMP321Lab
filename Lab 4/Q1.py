# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:14:40 2022

@author: rohan
"""

'''
Write a Polygon class that is a sequence of 2D points represented by named tuples, so that each point is given a name e.g., point ‘A’  is (4, 5).  The class defines the following functions:

a.	Polygon initialization, printing, length, and membership:
1.	An initializer that takes three or more points as arguments e.g., Polygon(('A',5,0), ('B',10,5), ('C',5,10), ('D',-2,8)), and defines a polygon accordingly.
2.	A function that allows using print e.g., print(poly), to output all points of a polygon in the following format: A: (5,6) -> B: (6,7) -> C: (12,15)
3.	A function that returns the number of points in the polygon, so that len(poly) works.
4.	A membership function that checks if a given point is in the polygon, or not.

'''

'''
b.	Point insertion, retrieval, and removal, polygon comparison: 
1.	 An insert function that inserts at the given index a new point from given name and x, y coordinates. It should throw a user defined exception ExistingPointError if the point exists. Check the name of the point as well as x and y coordinates. 
2.	A get function that allows retrieving a point given its name. The function should throw a user defined exception PointNotFoundError if such point does not exist.
3.	A remove function that deletes a point by name. Throws PointNotFoundError.
4.	A function that implements comparison, so that poly1==poly2 works. Two polygons are the same if and only if they contain the same points in the same order. 

'''

'''
c.	Polygon drawing:
1.	A function that draws a polygon on the screen, using Turtle graphics. 
For more info about Turtle graphics, see 
 https://docs.python.org/3/library/turtle.html  

'''
from collections import namedtuple
import turtle
Point = namedtuple('Point', 'name x y')


class Polygon:
    def __init__(self,*args):
        if len(args)<3:
            print("Error! Too few arguments passed in for a polygon!")
            #Should throw exception here
            return
        self.points=[]
        for pt in args:
            self.points.append(pt)
        
    def __str__(self):
        res=''
        for pt in self.points:
            if pt == self.points[-1]:
                res+=f'{pt.name}: ({pt.x},{pt.y}) '
            else:
                res+=f'{pt.name}: ({pt.x},{pt.y}) -> '
        return res

    def __len__(self):
        return len(self.points)
    
    def __contains__(self,pt):
        return pt in self.points
    
    ############################# part b #############################
    def insert(self,index,p):
        for pt in self.points:
            if pt.name==p.name and pt.x==p.x and pt.y==p.y:
                raise ExistingPointError #TBD
                return 
        self.points.insert(index,p)
        
    def getPoint(self,name):
        for pt in self.points:
            if pt.name==name:
                return pt
        raise PointNotFoundError #TBD
        
    def remove(self,p):
        for pt in self.points:
            if pt.name==p.name:
                self.points.remove(pt)
                return
        raise PointNotFoundError #TBD
        
    def __cmp__(self,rhs):
        if len(self.points)!=len(rhs.points): return False
        for pt1,pt2 in zip(self.points,rhs.points):
            if not(pt1.x==pt2.x and pt1.y==pt2.y):
                return False
        return True
    
    ############################# part c #############################
    
    def draw(self):
        turtle.speed(50)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto((self.points[0].x,self.points[0].y))
        turtle.pendown()
        turtle.color('red')
        turtle.write(self.points[0].name)
        for pt in self.points[1:]:
            turtle.goto((pt.x,pt.y))
            turtle.write(pt.name)
                
        turtle.exitonclick()


#Driver provided:
p= Polygon(Point('A',0,50),Point('B',300,150),Point('C',400,300))

p.insert(len(p),Point('D',450,100))
p.insert(len(p),Point('E',470,200))

print("Testing getPoint: ", p.getPoint('B'))
print("Testing len: ", len(p))
print(p)
p.remove(Point('B',300,150))
print(p)
print( "Testing in ",  Point('A',0,50) in p )

p1= Polygon(Point('A',0,50),Point('B',300,150),Point('C',400,300))

print(p1)
print(p1==p)

p.draw()
