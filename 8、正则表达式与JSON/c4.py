""" 概括字符集 """
import re

Str_demo = "this is a demo, it has 1?2.3/\d'#@!', \t\n  tab\
enter."

print('\d: ', re.findall('\d', Str_demo))
print('\D: ', re.findall('\D', Str_demo))
print('\w: ', re.findall('\w', Str_demo))
print('\W: ', re.findall('\W', Str_demo))
print('\s: ', re.findall('\s', Str_demo))
print('\S: ', re.findall('\S', Str_demo))
print('.: ', re.findall('.', Str_demo))

# tab键打出来的被认为是空格, 换行打出来没有显示，\t, \n显示为tab和换行, 输入时的换行和tab并不能被字符串接收为
# 有效信息。