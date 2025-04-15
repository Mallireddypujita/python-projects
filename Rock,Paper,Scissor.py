import random

options=["rock","paper","scissors"]
user=input("Enter rock,paper,scissors : ")
computer=random.choice(options)
print(f"user choice:{user}")
print(f"computer choice:{computer}")

#conditions to decide winner
if  user==computer:
    print("Tie")
elif (user =="rock" and computer =="scissors") or (user=="paper" and computer =="rock") or (user=="scissors" and computer =="paper"):
    print("You Win")
else:
    print("computer Win")    
