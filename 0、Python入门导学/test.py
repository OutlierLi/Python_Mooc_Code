'''
    如何交换两个变量
'''

# 其他语言：
x = 1
y = 2
print("交换之前的x,y的值分别为：" + str(x) + "," + str(y))
temp = x
x = y
y = temp
print("交换之后的x,y的值分别为：" + str(x) + "," + str(y) + "\n")
# 具有pythonic风格的代码：
a,b = 1,2
print("交换之前的a,b的值分别为：" + str(a) + "," + str(b))
a,b = b,a
print("交换之后的a,b的值分别为：" + str(a) + "," + str(b))

