# map类的使用

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

def square(x):
    return x*x

# for x in list_x:
#     print(square(x))
if(__name__ == '__main__'):
    r = map(square, list_x)
    print(r) # r是一个map类对象，可以转换为列表
    print(list(r))

    r = map(lambda x: x*x, list_x)
    print(list(r))

    list_y = [1, 2, 3, 4, 5, 6, 7, 8]
    # list_y = list_x # 注意，如果在此处定义list_y，且在后面修改list_y，list_x也会随之改变
    list_y[0:0] = [0, 0, 0]
    print(list_y, list_x)
    r = map(lambda x, y: x*x + y, list_x, list_y)
    print(list(r))