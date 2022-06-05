# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:15:04 2022

@author: Dell
"""

import math
print((3+4)*5)
n=int(input("enter the number"))
exp2=n*(n-1)/2
print(exp2)
r=int(input("enter the value of radius"))
exp3=4*3.14*r
print(exp3)
 
a=float(input("enter the angle of cos"))
b=float(input("enter the angle of sine")) 
exp4= math.sqrt(r*math.cos(a)**2+r*math.sin(b)**2)
print(exp4)
y1=float(input("enter the 1st y coordinate"))
y2=float(input("enter the 2nd y coordinate"))
x1=float(input("enter the 1st x coordinate"))
x2=float(input("enter the 2nd x coordinate"))
exp5=(y2-y1)/(x1-x2)
print(exp5)