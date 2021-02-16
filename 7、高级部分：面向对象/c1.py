class Student():
    name = 'student'
    age = 18
    __score = 100
    score = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = self.__class__.__score
    
    # 类方法
    @classmethod
    def demo_use(cls):
        cls.age = 20 # cls也是一个可以改变名字的参数，和self类似
        # 只能有一个参数为cls
        print(cls.__dict__)

    def print_demo(self):
        print("name: " + self.name)
        print("age: " + str(self.__class__.age))
        # 实例方法也可以实现对类变量的操作

    # 静态方法
    @staticmethod
    def demo_static(name):
        print("这是一个静态方法！")
       # self.name = 1 不可以传入self

    # 私有方法
    def __demo_private():
        print("this is a private!")

student = Student('Li', 19)
student.print_demo()
student.demo_use() # 类方法也要引用执行
student.print_demo()
student.demo_static(1)


print(student.name)
# print(student.__score) 
# 无法访问
# student.__score = 99 # 相当于新增了一个变量名字为__score
# print(student.__score)
# print(student.score)

print(student.__dict__)
print(student._Student__score) # Python自动修改名字,无论是类变量还是构造方法中的私有变量都被改了名字
student.demo_use()
# student._Student__demo_private() 
# 即使改了方法的名字依旧无法访问


