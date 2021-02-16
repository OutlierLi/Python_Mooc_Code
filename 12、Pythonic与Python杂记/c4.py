# 生成器
# print 0~10000

# 不是生成器生成，列表推导式的应用
n = [i for i in range(0, 10001)] # range函数，第一个参数计入，第二个参数不计入
# for i in n:
#     print(i)

# 生成器
def gen(max):
    n = 0
    while n <= max:
        print(n) # 直接print,糟糕的代码,对数字进行了操作，不是一个生成器
        n+=1

# gen(100)

def gen1(max):
    n = 0
    while n <= max:
        n += 1
        yield n

print(gen1(100)) # 返回的是一个生成器
go = gen1(10)
print(next(go))

for i in go:
    print(i) # 注意由于前面已经打印了1，所以在此从2开始打印


