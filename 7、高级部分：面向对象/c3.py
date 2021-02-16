from c2 import People
class Man(People):
    sum = 0
    def __init__(self, work, name, age):
        super().__init__(name, age)
        # super(Man, self).__init__(name, age)
        # People.__init__(self, name, age) # 父类构造函数调用时写入self的变量也写入了子类的self中
        self.work = work # name和age通过父类写入self

    def print_demo(self): # 注意要传入self
        super().print_demo() # 实例方法可以调用
        super().static_demo() # 静态方法可以调用
        super().class_demo() # 类方法无法调用
        super().__private_print() # 私有方法无法调用


    
man = Man('doctor', 'Li', 18)
man.print_demo()
print(man.__dict__)