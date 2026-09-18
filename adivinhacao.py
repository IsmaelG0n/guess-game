import random

secret = random.randint (1, 100)
guesses = 0
max_attempts = 7

# Sistema para adivinhar o número
while guesses < max_attempts:

    guess = int(input("Guess a number (1-100): "))
    guesses += 1

    if guess < secret:
        print("Too low")

    elif guess > secret:
        print("Too high")

    else:
        print(f"Got it in {guesses} guesses")
        break

else:
    print(f"You've used all {max_attempts} guesses. The secret number was {secret}.")
