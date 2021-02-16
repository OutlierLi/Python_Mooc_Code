import re

a = 'PythonPythonPythonPythonPythonPython'

r = re.findall('(Python){3}', a)
print(r) # 注意返回的是Python，而不是三个Python

lanuage = 'PythonC#\nJavaPHP'
r = re.findall('c#', lanuage, re.I) # 不区分大小写的匹配
print(r)

r = re.findall('c#.{1}', lanuage, re.I)
print(r)
r = re.findall('c#.{1}', lanuage, re.I | re.S) # 不区分大小写，且使.可以匹配换行符
print(r)

r = re.sub('C#', 'GO', lanuage, 0)
print(r)

a = lanuage.replace('C#', 'GO')
print(a)

def convert(value):
    print(value)
    print(value.group())
    pass

r = re.sub('C#', convert, lanuage)
print(r)


