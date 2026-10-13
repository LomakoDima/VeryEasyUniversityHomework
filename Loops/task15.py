import random

secret_number = random.randint(1, 100)
attempts = 7

while attempts > 0:
    guess = int(input("Guess the number (1-100): "))

    if guess == secret_number:
        print("Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1

    if attempts > 0:
        print("Attempts left:", attempts)
else:
    print("Game over! The number was", secret_number)
