# 海象运算符

a = 'python'

if (b:=len(a)) > 5:
    print('长度大于5；'+'真实长度为：'+str(b))

# b = len(a)
# print('长度大于5；'+'真实长度为：'+str(b)) # 代替部分

# 避免了函数求值，减少了性能浪费

# f关键字做字符串拼接
b = len(a)
print(f'长度大于5；真实长度为：{b}') # {}内为变量，整体是一个字符串，外面有一个f关键字
