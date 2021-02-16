# 算术运算符 + - * / // % **

# 赋值运算符 = += -= /= %= //= **= *=

# 比较运算符
a = 1
a += a >= 1
print(a)
print('a' > 'b')
print('abc' < 'abd')
print([1,2,3] < [2,3,4])

# 逻辑运算符
print(1 and 2)
print(0 and 1)
print('a' or 'b')
print('' or 'b')
print(not 'a')

# 成员运算符
1 in [1,2]
2 not in [1,3]
2 in {1:3, 2:4}

# 身份运算符(id判断)
a = 1
b = 2
c = 1
d = 1.0
print(a is b)
print(a is c)
print(a is d)
print(a == d)
x = {1, 2, 3}
y = {1, 1, 2, 3}
z = {2, 1, 3}
print(x == y)
print(x is y)
print(x == z)
print(x is z)

# 位运算符 & | ^ ~ << >>
print(0b11 & 0b10)
print(3 & 2)
