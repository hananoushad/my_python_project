import random
choice=["stone","paper","scissor"]
print(choice)
y=random.choice(choice)
while True:
    x = input("enter your choice:").lower()
    if x != "stone" and x != "paper" and x != "scissor":
        print("enter a correct choice")
    else:
        break
print("your choice is", x)
print("computer choice is", y)
if x == y:
    print("its a draw")
elif x == "scissor" and y == "stone":
    print("you win")
elif x == "scissor" and y == "paper":
    print("you win")
elif x == "paper" and y == "stone":
    print("you win")
else:
    print("you lose")










