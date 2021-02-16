class People():
    name = ''
    age = 20

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("this is __init__!")

    def print_demo(self):
        print("name: " + self.name)
        print("age: " + str(self.age))

    def __private_print():
        print("this is private_print!")

    @staticmethod
    def static_demo():
        print("this is staitc_demo!")

    @classmethod
    def class_demo():
        print("this is class_demo!")

