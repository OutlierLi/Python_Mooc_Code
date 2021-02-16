# 列表推导式
a = [1, 2, 3, 4]
b = [i*i for i in a]
print(b)
print(id(a), id(b)) # 虽然b是由a推导而来，但是他们是两个不同id的列表

c = [i*i for i in a if i>=5]
print(c)
d = [(lambda x: x*2)(i) for i in a]
print(d) # 将第一参数换成lambda表达式，也就是说第一个参数可以是一个函数

# 字典的列表推导式
students = {
    'Li' : 18,
    'Gao' : 20,
    'Zhao' : 15
}

students1 = {key:value for key,value in students.items()}
print(students1)

# 元组的列表推导式
ayuan = (1, 2, 3)
byuan = (i for i in ayuan)
print(byuan) # generator对象，不会直接打印元组
