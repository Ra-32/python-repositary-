# marks=[32 ,13, 54, 76]
# print(marks)


# student=["rahul", 91,91.0 ,3+4j]
# print(student)

marks=[98,64,33,95,76]
# print(marks[1:])
# print(marks[::-1])

# marks.append(31)
# marks.sort(reverse=True)
# marks.insert(2,43)
# marks.remove(31)
# marks.pop(2)

# print(marks)

# tup=("rahhul",32,98,71.4)

# print(tup.index(32))
# 
# print("hello")
# list=[]

# for i in range(4):
#     movie= input(f"enter the movie {i} ")
#     list.append(movie)

# print(list)

# marks=["rahul","mom",1,2,3,2,1]

# tup=(1,2,3,4)

# print(tup)
# print(tup.count(1))
# print(tup.__add__)


# list1=["C","D","A","A","B","B","A"]

# tup=tuple(list1)

# print(tup.count("A"))


# print(tup[2])

# dictionary

rk={
    "rahul":"kapade",
    "marks":{
        "sem1":9.6,
        "sem2":9.3,
        "sem3":9.54
    }   
}

# print(rk)
# print(rk.values())
# print(rk.items())
# print(rk.get("rahul"))
# print(rk.keys())

# set2={1,2,45,67,89,32}
# print(set2.add(47))
# print(set2.difference())
# print(set2.pop())
# print(set2.clear())

# 3
result = {}

def student(x,y,z):
#   result = {}
   result[user_no] = [std_name, marks]
   print(result)

print(result)
n = int(input("Enter No of Students:"))
for i in range(n):

   user_no = int(input("user No: "))
   std_name = input("user Name: ")
   marks = int(input("Marks: "))
   student(std_name, user_no, marks)
