# 元组的类型
print(type((1,2,3,4,5)))

# 元组元素访问
a = (1, 2, 3, 4)
print(a[0])
print(a[0:2])

# 元组的相加相乘
print(a + (5, 6))
print(a * 2)

# 一个特殊的元组，只有一个元素的元组
print(type((1)))
print(type((1,)))

# 空元组的定义
print(type(()))
