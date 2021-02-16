from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4 # 常量建议大小全部字母
    # YELLOW = 5 # 标签不能重复
    PINK = 1 # 数值重复的会被第一个标签覆盖,覆盖指的是id覆盖和值覆盖, PINK相当于别名


print(VIP.YELLOW)
print(VIP.PINK)

# VIP.BLACK = 4 # 不可以直接改变标签的值

print(VIP.YELLOW.value)
print(VIP.YELLOW.name)

print(type(VIP.BLACK))
print(type(VIP.BLACK.name))
print(type(VIP.BLACK.value))

print(VIP['YELLOW'])

for v in VIP:
    print(v)

print(VIP.GREEN == VIP.GREEN)
print(VIP.PINK == VIP.YELLOW)

print(VIP.PINK is VIP.YELLOW)

# 打印别名
for v in VIP.__members__.items():
    print(v)

for v in VIP.__members__:
    print(v)
    print(type(v)) # 是字符串类型，而不是类对象

print(VIP(1)) # 注意，这里的1代表的不是序号1，而是枚举类型的值为1
