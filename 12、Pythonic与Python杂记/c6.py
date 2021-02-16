# 装饰器的副作用

import time
from functools import wraps

def decorator(func):
    @wraps(func) # 装饰器可以使函数返回原名
    def wraapper():
        print(time.time())
        func()
    return wraapper

@decorator
def f4():
    print(f4.__name__) # f1的名字并不是f1而是wrapper

f4()
