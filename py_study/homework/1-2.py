from math import *
x1,y1,x2,y2=map(int,input('请输入两点坐标:').split())
d=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
print('距离为:',sqrt(d))
