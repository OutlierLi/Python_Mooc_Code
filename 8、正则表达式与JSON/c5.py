import re

a = 'python 1111java678php'

r = re.findall('[a-z]', a)
print(r)

r = re.findall('[a-z]{3}', a)
print(r)

r = re.findall('[a-z]{3,6}', a)
print(r)

r = re.findall('[a-z]{3,6}?', a)
print(r)
