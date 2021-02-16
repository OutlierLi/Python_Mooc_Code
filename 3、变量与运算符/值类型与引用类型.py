# 值类型
a = 1
b = a
c = 1
print(id(a))
print(id(b))
print(id(c))
a = 3
print(id(a))
print(b)
print(id(b))

# 引用类型
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(id(x))
print(id(y))
print(id(z))
y[0] = 'y'
print(x)
print(id(x))
print(id(y))

strs = 'hello '
print(id(strs))
strs += 'world'
print(id(strs))

# 在列表中追加一个元素
x.append(4)
print(x)

# 修改元组中列表的元素
t = (1, 2, [3, 4])
t[2][0] = 'z'
print(t) 
