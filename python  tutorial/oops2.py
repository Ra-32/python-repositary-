# del key word

# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("rahul")
# print(s1.name)
# del s1.name
# print(s1.name)

#private  

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass= acc_pass # make it private __

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1=Account("1234","abcde")


# print(acc1.reset_pass())




# # inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")


    
# class ToyotoCar(Car):
#     def __init__(self,brand):
#         self.brand=brand


# class Fortuner(ToyotoCar):
#     def __init__(self, type):
#         self.type=type




# car1=Fortuner("diesel")
# car1.start()
# print(car1.type)


class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()

print(c1.varC)
print(c1.varA)
print(c1.varB)