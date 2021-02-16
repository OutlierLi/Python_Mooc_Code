# 集合的类型
print(type({1,2}))

# 集合的定义
a = {1,2,3,4,5,6}

b = {1,1,1,2}
print(b) # 集合内部元素不重复

# len函数
len(b)

# in运算符
1 in a

# 减法操作（差集）
print(a - {6})

# 集合的交集运算
print({1,2,3} & {1})

# 集合的并集运算
print({1,2} | {3,4})

# 特殊集合空集合的定义
print(type({}))
print(type(set()))
print(len(set()))
