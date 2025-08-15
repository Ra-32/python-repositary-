import random
target= random.randint(1,100)

while True:
    userchoice=input("guess the number or Quit(Q):")
    if(userchoice == "Q"):
        
        break
    
    userchoice=int(userchoice)
    if(userchoice == target):
        print("Sucess you won!!")
        break
    elif(userchoice < target):
        print("your number is small,Take a bigger guess...")
    else:
        print("your number is big,Take a smaller  guess...")

print("GAME OVER !!!....")



