import random

number = random.randint(1, 100)

print("Number Guessing Game")
print("You have 3 tries to guess the number between 1 and 100")

for attempt in range(1, 4):

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed the number.")
        break

    elif guess > number:
        print("Too high")

    else:
        print("Too low")

    print("Attempts left:", 3 - attempt)

if guess != number:
    print("Game Over. The number was:", number)
