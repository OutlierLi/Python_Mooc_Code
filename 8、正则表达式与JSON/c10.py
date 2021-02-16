import re

s = 'life is short, i use python'
r = re.search('life(.*)pyth(\w)n', s)
print(r.group(0))
print(r.group(1))
print(r.group(0,1)) # 返回是一个元组
print(r.groups())

# r = re.findall('life(.*)pyth(.)n', s)
# print(r) # 列表中的一个元组



