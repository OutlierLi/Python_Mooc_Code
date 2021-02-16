# 函数的定义
def funcname(parameter_list):
    pass

def add(x, y):
    result = x + y
    return result

c = add(1, 2)
print(c)

d = funcname(1)
print(d)

def test():
    print("1")
    return
    print("2")

e = test()

def test_another():
    a = 1
    b = 2
    return a,b

f = test_another()
print(f)
print(type(f))

# 序列解包
skill_1st, skill_2ed = test_another()
print(skill_1st, skill_2ed)

# 链式赋值
t = 1,2,3
print(t)
print(type(t))
t1, t2, t3 = t
print(t1, t2, t3)

# 可变参数
def demo(*param):
    print(param)
    print(type(param))

demo(1,2,3)
demo_param = (1,2,3)
demo(demo_param)
demo(*demo_param)
demo_param2 = [1,2,3] # 列表也可以通过类似序列解包方式传入函数，传入后还是元组的形式
demo(*demo_param2)

# 关键字可变参数
def city_temp(**param):
    print(param)
    print(type(param))
    pass

city_temp(beijing='32c', shanghai='33c') # 字典
# 将字典平铺进函数
demo_dict = {'1':1, '2':2}
city_temp(**demo_dict)
# key必须是字符串类型？！
