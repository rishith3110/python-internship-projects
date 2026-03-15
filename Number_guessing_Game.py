import random

guess_number = random.randint(1,100)
count = 0

while True:

    user_number = int(input("please enter the number to guess: "))
    count += 1

    if(user_number == guess_number):
        print("Congratulations! You have matched the guess number!")
        print("Total attempts:",count)
        break

    elif(abs(user_number - guess_number) == 1):
        print("Very very close to the number!")

    elif(abs(user_number - guess_number) <= 5):
        print("You are close to the number")

    elif(abs(user_number - guess_number) <= 10):
        print("You are little bit far from the number")

    else:
        print("Too far! Try again")