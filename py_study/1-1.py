from math import *
from decimal import Decimal
a,b,c=map(float,input('请输入三角形三边边长:').split(','))
if (a+b)>c and (b+c)>a and (a+c)>b:
    p=(a+b+c)/2
    area=sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积为:',Decimal(area).quantize(Decimal('0.00')))
else:
    print('输入的三边构不成三角形！')