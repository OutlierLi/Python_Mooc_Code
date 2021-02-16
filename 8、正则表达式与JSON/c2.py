""" 
    此处有一些疑问待解决！
"""
import re

a4 = 'c|c++|1Java|8Python|9JavaScript\\\\d'
a3 = 'c|c++|1Java|8Python|9JavaScript\\\d'
a2 = 'c|c++|1Java|8Python|9JavaScript\\d'
a1 = 'c|c++|1Java|8Python|9JavaScript\d'


# # for in 取出数字
# for numb in a:
#     if(numb >= '0' and numb <= '9'):
#         print(numb)

h = re.findall('\\\\\d', a1)
r = re.findall('\\\\d', a1)
f = re.findall('\\\d', a1)
d = re.findall('\\d', a1)
e = re.findall('\d', a1)
print(a1, h, r, f, d, e)

h = re.findall('\\\\\d', a2)
r = re.findall('\\\\d', a2)
f = re.findall('\\\d', a2)
d = re.findall('\\d', a2)
e = re.findall('\d', a2)
print(a2, h, r, f, d, e)

h = re.findall('\\\\\d', a2)
r = re.findall('\\\\d', a3)
f = re.findall('\\\d', a3)
d = re.findall('\\d', a3)
e = re.findall('\d', a3)
print(a3, h, r, f, d, e)

h = re.findall('\\\\\d', a2)
r = re.findall('\\\\d', a4)
f = re.findall('\\\d', a4)
d = re.findall('\\d', a4)
e = re.findall('\d', a4)
print(a4, h, r, f, d, e)

