import re

a = 'pytho0python1pythonn2'

# 0次或无穷次
r = re.findall('python*', a)
print(r)

# 1次或无穷次
r = re.findall('python+', a)
print(r)

# 0次或1次
r = re.findall('python?', a)
print(r)