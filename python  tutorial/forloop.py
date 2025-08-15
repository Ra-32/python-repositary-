# list=[1,2,3]
# veg=["potato",23,5,"rahul"]

# str="apnacollege"
# for i in str:
#     if(i=="o"):
#         print("o found")
#         break
#     print(i)
# else:
#     print("end")
# idx=0
# num=(1,4,9,16,25,36,49,64,81,100)

# x=36
# for idx in num:
#     if (idx==x):
#         print("foud at idx",idx)
#     idx += 1

# for i in range(2,100,2):
#     print(i)

# for i in range(100,0,-1):
#     print(i)
    
n=int(input("enter the number"))
# i=1
fact=1

# while i<=n:
#     fact*=i
#     i+=1

# print(fact)

for i in range(1,n+1):
    fact*=i

print(fact)
 