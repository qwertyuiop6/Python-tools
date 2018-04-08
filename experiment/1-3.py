from decimal import Decimal
from math import pi
r=float(input('请输入球半径r (单位:km):'))
s=4*pi*1e6*r*r
print('该球表面积为:',Decimal(s).quantize(Decimal('0.000000')),'m²')
print('1: δA=4π(r+δr)²-4πr²')
print('2: δA=8πr·δr')
print('3:  ')
method=input('----选哪种公式计算?:')
cmd='y'
while cmd!='n':
    r2=float(input('请输入半径增量δr(单位:mm):'))
    if method=='1':
        s2=4*pi*(2*1e3*r+1e-3*r2)*1e-3*r2
    elif method=='2':
        s2=8*pi*1e3*r*1e-3*r2
    else:
        s2=4*pi*(1e3*r+1e-3*r2)*(1e3*r+1e-3*r2)-4*pi*1e3*r*1e3*r
    r+=r2
    s+=s2
    print('表面积增量为:',Decimal(s2).quantize(Decimal('0.000000')),'m²')
    print('当前表面积为:',Decimal(s).quantize(Decimal('0.000000')),'m²')
    cmd=input('继续吗?(y/n):')

