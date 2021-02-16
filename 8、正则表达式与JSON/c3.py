import re

S = 'abc, acc, adc, aec, afc, ahc' # 找出单词中间字符是c或f的单词

r = re.findall('a[cf]c', S)
print(r)

# 匹配非c和非f的单词
a = re.findall('a[^cf]c', S)
print(a)

# 匹配顺序字符
b = re.findall('a[cdef]c', S)
c = re.findall('a[c-f]c', S)
print(b, c, b == c)

