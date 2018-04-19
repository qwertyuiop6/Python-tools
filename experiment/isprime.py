# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:04:19 2018

@author: shadow
"""

def isPrime(num):
    try:
        if num<=1:
            return False
        else:
            m=2
            while m*m<=num:
                if num%m==0:
                    return False
                m+=1
            return True
    except TypeError:
        print('请输入一个整数！')

num=int(input('输入一个整数:'))
print(isPrime(num))
