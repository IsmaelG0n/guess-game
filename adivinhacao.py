import random

secret = random.randint (1, 100)
guesses = 0

# Sistema para adivinhar o número
while True:

    guess = int(input("Guess a number (1-100): "))
    guesses += 1

    if guess < secret:
        print("Too low")

    elif guess > secret:
        print("Too high")

    else:
        print(f"Got it in {guesses} guesses")
        break

    # criar um commit apenas para testar a conexão com o GitHub