# class Car:
#     def __init__(self,type):
#        self.type=type 


#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")


    
# class ToyotoCar(Car):
#     def __init__(self,type,name):
#         super().__init__(type)
#         self.name=name

# car1=ToyotoCar("tesla","ev")

# print(car1.type)
# print(car1.start())



# class Person:
#     name="kapade"

#     @classmethod # decorater
#     def changeName(cls,name):
#         cls.name=name


# p1=Person()
# p1.changeName("kapade rahul")
# print(p1.name)
# print(Person.name)







class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        # self.percentage=str((self.phy+self.chem+self.maths)/3)+"%"

    @property # decorater
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+ "%"

stu1=Student(98,97,96)
# print(stu1.phy)
# print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
print(stu1.percentage)

stu1.chem=90
print(stu1.chem)
print(stu1.percentage)
        
#decorater

# @staticmethod
# @classmethod
# @property
# @getter 
# @setter

