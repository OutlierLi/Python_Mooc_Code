a = 1
b = 2

# global关键字
def demo():
    global a
    a = 2
    b = 3

demo()
print(a)
print(b)
