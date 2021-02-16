a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (start_index, end_index, step) 默认step为1

# 切取单个值
print(a[0])
print(a[-4])

# 切取完整对象（因为返回的是一个列表对象，而不是一个值）
print(a[:]) 
print(a[::]) # 从左往右
print(a[::-1]) # 从右往左

# 方向与前两个变量冲突时，返回空列表
print(a[1:6:-1])
print(a[6:1])

print(a[:6:-1]) # 从右往左，从末尾开始，到end_index=6停止
print(a[6:]) # 从左往右，从start_index=6开始
print(a[6::-1]) # 从右往左，从start_index=6开始
# 没有指定start_index或end_index,由step决定其是从第一个还是最后一个开始

# 连续切片操作
print(a[:8][2:5][-1:]) # 理论上可以无限切片

# 切片操作参数可以用表达式
a[2+1:3*2:7%3]

# 利用range函数生成1-99的整数，然后取3的倍数，再最后取十个
for i in range(1, 100)[2::3][-10:]:
    print(i)

'''
    常用切片操作
'''

# 取偶数位置
a[::2]

# 取奇数位置
a[1::2]

# 拷贝整个对象（浅拷贝）
b = a[:]
print(b)
print(id(a))
print(id(b)) # 等同于copy函数

# 修改单个元素
a[3] = ['A', 'B']

# 在某个位置插入元素
a[3:3] = ['A', 'B', 'C']

# 替换一部分元素
a[3:6] = ['A', 'B']

# start_index与end_index之间没有必然的大小关系，如何走取决于step
