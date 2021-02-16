'''
    这是一个注释
'''
import seven1


infos1 = dir(seven1)
print(infos1)

infos = dir()
print(infos)
'''
    这是一个注释
'''
# 这是一个注释
print("name:" + __name__)
print("package:" + (__package__ or '入口文件不属于任何包'))
print("file:" + __file__)
print("doc:" + (__doc__ or '当前没有注释文件'))

print("name:" + seven1.__name__)
print("package:" + (seven1.__package__ or '入口文件不属于任何包'))
print("file:" + seven1.__file__)
print("doc:" + (seven1.__doc__ or '当前没有注释文件'))

if __name__ == '__main__':
    print("这是入口文件") # 可以区别作为模块引用的代码和作为执行函数的代码
