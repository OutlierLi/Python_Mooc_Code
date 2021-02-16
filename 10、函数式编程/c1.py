# lambda表达式

def add(x, y):
    return x + y

f = lambda x,y: x + y
print(add(1, 2) == f(1, 2))

x = 0
y = 1
r = x if x > y else y
print(r)

