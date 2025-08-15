# a=5
# b=10
# function defination
# def sum(a,b):
#     print(a+b)

# sum(5,10)

# avg of 3 num

# def avg(a,b,c):
#     avr=a+b+c/3

#     return int(avr)

# mean= avg(2,3,4)
# print(mean)

cities=["mum","pune","kol"]
num=(1,4,9,16,25,36,49,64,81,100,36)
def print_len(cities):
    print(len(cities))


def print_name(list):
    for i in list:
        print(i,end=" ")

def facto(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")



def fact_o(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact_o(n-1)


def cal_sum(n):
    if n==0:
        return 0
    return cal_sum(n-1) + n

ans=cal_sum(5)
print(ans)
