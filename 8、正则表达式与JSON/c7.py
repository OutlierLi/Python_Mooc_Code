import re

a = '1808851818'

r = re.findall('\d{5,12}', a)
print(r)

# 边界匹配
r = re.findall('^\d{5,12}$', a)
print(r)