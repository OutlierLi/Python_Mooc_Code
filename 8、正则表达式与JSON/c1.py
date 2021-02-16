import re

a = 'c|c++|Java|Python|JavaScript'
print(a.index('Python'))
print(a[11])
print('Python' in a)

r = re.findall('Python', a)
print(r) # 列表


