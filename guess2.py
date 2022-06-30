
import os
answer = int(input("What should the answer be? "))
guesses = int(input("How many guesses? "))
os.system('cls||clear')

guess_count = 0
guess = int(input("Guess a number: "))
guess_count += 1
guess_left=guesses-guess_count
print("Guesses left",guess_left)

if answer < guess:
    print("The number is lower than that.")
elif answer > guess:
    print("The number is higher than that")

while guess != answer and guess_count < guesses:
    guess = int(input("Guess a number: "))
    guess_count += 1
    if answer < guess:
        print("The number is lower than that.")
        print(guess_left)
    elif answer > guess:
        print("The number is higher than that")
        print(guess_left)
if guess_count >= guesses and guess != answer:
    print("You lose; the number was " + str(answer) + ".")
if guess == answer:
    print("You win!")
