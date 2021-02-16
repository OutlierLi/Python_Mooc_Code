a = ''
print(not a)
print(a is None)
b = '1'
print(not b)
print(b is None)

# is None 与 空不同

# 对象存在不一定为True
class Test():
    def __len__(self):
        return 0

    def __bool__(self):
        return True
        # return 1 # 不能是其他类型，只能是严格的布尔类型
    pass

test = Test()
if test:
    print('test is True')
else:
    print('test is False')

