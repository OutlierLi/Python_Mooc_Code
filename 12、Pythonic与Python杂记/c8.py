# 数据类dataclass装饰器

from dataclasses import dataclass
@dataclass(init = True, repr = True) # 生成的函数是可控的
class Student():
    name : str
    age : int
    school_name : str
    # def __init__(self, name, age, school_name):
    #     self.name = name
    #     self.age = age
    #     self.school_name = school_name
    #     # 这三条语句结构一样，重复了三遍，很呆板
    
    def test(self):
        print(self.name)

student = Student('Li', 20, 'XDU')
student.test()

print(student.__repr__()) # 不仅可以生成构造函数，还可以生成某些魔术方法(repr方法)
