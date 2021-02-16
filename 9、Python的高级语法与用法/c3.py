def curve_pre():
    a = 25 # 环境变量a
    def curve(x):
        print("这是一个闭包函数！")
        return a*x*x
    return curve # 返回的是一个闭包，而不仅仅是一个函数

f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
a = f(2)
print(a)