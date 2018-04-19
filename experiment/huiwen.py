# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:24:26 2018

@author: shadow
"""

def ishui(num):
    a=len(num)
    b=int(a/2)
    while b>=0:
        if num[b]!=num[-(b+1)]:
            return False
        b-=1
    return True

def ishui2(num):
    num2=num[::-1]
    return num==num2
        
num=input('请输入一个整数:')
print(ishui2(num))