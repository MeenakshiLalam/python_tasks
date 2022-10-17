import random

num = random.randint(1, 9)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 9 : \n "))

    if guess >num  :
        print("you entered too high number")
    elif guess < num:
        print("you entered too low number ")
    elif guess == num :
        print("congratulations! you won!")
        break
    else:
        print(" sorry try again!")