# 带参数的函数使用装饰器
import time

def decorator(func):
    def wraapper(*args): # 加入可变参数
        print(time.time())
        func(*args)
    return wraapper

@decorator
def f1(func_name):
    print('this is ' + func_name)

f1('Li')

