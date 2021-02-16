a = 'hello'
print(type(a) == str)

# isinstance函数判断
b = isinstance(a, str)
print(b)
c = isinstance(a, (int, float, list)) # 三选一
print(c)