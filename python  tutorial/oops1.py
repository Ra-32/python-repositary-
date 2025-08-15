# class Student:
#     #default constructor
#     def __init_(self):
#         pass

#     college_name="terna college" # common attribute class attribute

#     # paramterized constructor
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
        
#     def welcome(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.marks

    

# s1=Student("rahul",97)
# print(s1.name,s1.marks)
# s1.welcome()
# print(s1.get_marks())

# s2=Student("kapade",98)

# print(Student.college_name)





# class Student:
#     def __init__(self,name,marks):
#        self.name=name
#        self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is :",sum/3)

#     @staticmethod # decorater
#     def college():
#         print("terna college")


# s1=Student("tony",[98,97,96])
# s1.get_avg()

# s1.name="rahul"
# s1.get_avg()
# s1.college()




class Car():
    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch=False

    def start(self):
        self.clutch= True # abstraction
        self.acc= True
        print("car started...")


s1=Car()


class Account():
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    
    def debit(self,amount):
        self.bal -= amount
        print("Rs",amount,"was debited")
        print("total balance",self.get_balance())

    def credit(self,amount):
        self.bal += amount
        print("Rs",amount,"was credited")
        print("total balance",self.get_balance())
        

    def get_balance(self):
        return self.bal


acc1=Account(3000,4321)
print(acc1.bal)
print(acc1.acc)
acc1.debit(500)
acc1.credit(600)

acc1.credit(54000)
acc1.debit(1899)
