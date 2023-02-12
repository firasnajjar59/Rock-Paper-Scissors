import random
import asciArt
print(asciArt.logo)
print("choose 0 for rock, 1 for scissors, 2 for paper")
user_choice=input("")
computer_choice=random.randint(0,2)
if user_choice=="0" or user_choice=="1" or user_choice=="2":
    user_choice=int(user_choice)
    if computer_choice==user_choice:
        if user_choice==0:
            print(asciArt.rock)
            print(asciArt.rock)
        if user_choice==1:
            print(asciArt.scissors)
            print(asciArt.scissors)
        if user_choice==2:
            print(asciArt.paper)
            print(asciArt.paper)
        print("draw")
    elif user_choice==0:
        print(asciArt.rock)
        if computer_choice==1:
            print(asciArt.scissors)
            print("you win")
        else:
            print(asciArt.paper)
            print("you lose")
    elif user_choice==1:
        print(asciArt.scissors)
        if computer_choice==2:
            print(asciArt.paper)
            print("you win")
        else:
            print(asciArt.rock)
            print("you lose")
    elif user_choice==2:
        print(asciArt.paper)
        if computer_choice==0:
            print(asciArt.rock)
            print("you win")
        else:
            print(asciArt.scissors)
            print("you lose")
else:
    print("something went wrong please try again")
