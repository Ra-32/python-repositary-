import string 
import random


# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

pass_len=int(input("enter the password length"))

charchoice=string.ascii_letters+string.digits+string.punctuation
# password=""
# for i in range(pass_len):
#     password += random.choice(charchoice)

# print("your random password is:",password)


# list comprehension
password="".join([random.choice(charchoice) for i in range(pass_len)])

print("your random password is:",password)
