class Student:
    def __init__(self,name,sex,phone):
        self.name = name
        self.sex = sex
        self.phone = phone
    def printData(self):
        print("姓名：",self.name)
        print("性别：",self.sex)
        print("电话：",self.phone)

class Person(Student):
    def __init__(self,name,sex,phone):
        Student.__init__(self,name,sex,phone)

x = Person("杨杨","男","12345678")
x.printData()