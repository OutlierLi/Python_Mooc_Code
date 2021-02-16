class class_name():
    pass

class Student():
    name = 'student'
    age = 18

    def __init__(self, name, age):
        self.__class__.name = name # name不会存入构造函数的__dict__中；
        # self.age = age

    def print_file(self):
        print('name: ' + self.name)
        print('name: ' + self.__class__.name)
        print('age: ' + str(self.age))
        print('age: ' + str(self.__class__.age))
        # self.__class__.name 与 self.name 不是一个变量，代表的意义也不同

student = Student('Li', 19)
student.print_file()
print(student.__dict__)
