# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:02:51 2018

@author: shadow
"""



def inc(s):
    s+=1
    return s
def dec(s):
    s-=1
    return s
    
if __name__=='__main__':
    m,n=map(int,input('输入inc次数和dec次数').split())
    s=0
    while m:
        s=inc(s)
        m-=1
    while n:
        s=dec(s)
        n-=1
    print(s)