# 装饰器

import time

def f1():
    print(time.time())
    print('This is a function')

# f1()

def f2():
    pass

def print_current_time(func):
    print(time.time())
    func()

# print_current_time(f2) # 为f2加时间戳

# 时间戳装饰器
# def decorator():
#     def wraapper():
#         print(time.time())
#     return wraapper

def f3():
    print('this is f3')

# f = decorator()
# f()
# f3() # 实现了时间戳打印

# 语法糖
def decorator(func):
    def wraapper():
        print(time.time())
        func()
    return wraapper

@decorator
def f4():
    print('this is f4')

f4()
