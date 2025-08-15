# polymorphism  operater overloading
# print(1+2)
# print("rahul"+"kapade")
# print([1,2,3]+[4,5,6])

# print(type([1,2,3]))

# print((2j+5)+(5j+7))

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     def add(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
    
    
# num1=Complex(2,3)
# num1.showNumber()

# num2=Complex(6,7)
# num2.showNumber()

# num3=num1.add(num2)
# num3.showNumber()

# num3=num1+num2
# num3.showNumber()  error so we use dunder function __add__,__sub__,__mul__,__mod__,__div__


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    
# num1=Complex(2,3)
# num1.showNumber()

# num2=Complex(6,7)
# num2.showNumber()

# num3=num1-num2
# num3.showNumber()

class Circle:
    pie=3.14
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        area= int(self.pie*self.radius*self.radius)
        return area
    
    def get_peri(self):
        peri=2*self.pie*self.radius
        return peri
    

# c1=Circle(7)
# print(c1.get_area())
# print(c1.get_peri())

class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print("role",self.role)
        print("dept",self.dept)
        print("salary",self.sal)

class Enginner(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("enginner","it","67,990")
        


# e1=Enginner("rahul",89)
# e1.showDetails()



class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,order2):
        return self.price > order2.price
        
ord1=Order("chips",90)
ord2=Order("tea",67)

print(ord1 > ord2)
