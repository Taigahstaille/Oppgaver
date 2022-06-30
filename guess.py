import os
num1=0
num2=0
num3=0
guesses=0

num1=input("Chose number:")
num2=input("How many tries:")

os.system('cls||clear')

num3=input("What is your guess?")

if num3==num1:
    print("You got it!")
else:
    print("Wrong Number!")
    if num3>num1:
        print("Your guess is to!")
    else:
        print("Your guess is to low")
        print("you have",guesses,"left!")