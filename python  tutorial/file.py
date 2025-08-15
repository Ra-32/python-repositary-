# f=open("file_name or path ","mode")
# f= open("demo.txt","a")


# line1=f.readline()
# print(line1)

# f.write("\nchal labdya tuzi ai gal")
# f.close()

# with

# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# import os

# os.remove("demo.txt")
count=0
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            print("even")
            count+=1
    print(count)