# 一个非闭包事例
from typing import get_origin


def f1():
    a = 10
    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()

# 另一个非闭包事例
origin = 0

def go(step):
    global origin # 声明为全局变量
    new_pos = origin + step
    origin = new_pos
    return new_pos

print(go(2))
print(go(3))
print(go(6))

# 又一个事例闭包
origin = 0

def factory(pos):
    def go(step):
        nonlocal pos # 声明为非局部变量, 相当于在factory中定义了pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    # print(pos)
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(3))
print(tourist.__closure__[0].cell_contents)
print(tourist(6))
print(tourist.__closure__[0].cell_contents)
