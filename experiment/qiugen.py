# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:16:39 2018

@author: shadow
"""

#from scipy.optimize import root,fsolve
#from math import *

def f1(x):
    return pow(x,3)*2-4*x*x+3*x-6

#root1=fsolve(f1,[1.5])
#print(root1)

def f2(x):
    return 6*x*x-8*x+3


x=1.5
x2=0

while abs(x-x2)>1e-1:
    x2=x
    x=x2-f1(x)/f2(x)
print(x)