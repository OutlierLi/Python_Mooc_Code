import re

# 将大于等于6的替换为9，小于6的替换为0
s = 'A8C3721D86'
def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)
print(r)
r = re.match('\d', s) # 从字符串开始匹配
print(r)
r = re.search('\d', s) # 搜索整个字符串，直到第一个复合要求的字符
print(r)
print(r.span())
print(r.group())