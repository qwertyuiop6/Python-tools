from decimal import Decimal
from math import pi
radius=float(input('输入圆半径:'))
area=pi*radius*radius
print('圆面积为:',Decimal(area).quantize(Decimal('0.00')))