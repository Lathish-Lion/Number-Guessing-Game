import random

guessing_number = random.randint(1,100)
guessed=None
attempts=0

# print("Welcome to the Number Guessing Game!")
print("I have a number for you to guess between 1 and 100.")

while guessed!= guessing_number:
    try:
        guessed = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guessed < guessing_number:
            print("You came to the least man!")

        elif guessed > guessing_number:
            print("You came to the most man!")

        else:
            print(f"Congratulations buddy! You guessed the right number")

    except ValueError:
        print("Please enter a valid number between the given range.")