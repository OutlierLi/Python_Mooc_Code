# reduce的使用

from functools import reduce
from c2 import list_x

r = reduce(lambda x,y:x+y, list_x)
print(r)

list_xy = [(1,3), (2,-2), (-2,3), (1,1)]
result_xy = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), list_xy)
print(result_xy)

list_z = ['1', '2', '3', '4']
result_z = reduce(lambda x, y: x + y, list_z, 'aaa') # 设置一个初始值
print(result_z)