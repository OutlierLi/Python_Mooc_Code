# 存在关键字参数的函数使用装饰器

import time

def decorator(func):
    def wraapper(*args, **kw): # 加入可变参数 此装饰器传入参数事例可以解决几乎全部函数
        print(time.time())
        func(*args, **kw)
    return wraapper

@decorator
def f1(func_name, **param):
    print('this is ' + func_name)
    print(param)

f1('Li', bj='32c', sh='33c')