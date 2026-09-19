import random

#adicionar a escolha de dificuldade antes de iniciar o game.
difficulty = input ("Easy, Medium or Hard?").lower()

if difficulty == "easy":
        max_number = 50

elif difficulty == "hard":
        max_number = 1000

else:
     max_number = 100

secret = random.randint (1, max_number)
guesses = 0 # numero de tentativas
max_attempts = 7

# Looping para adivinhar o número
while guesses < max_attempts:

    guess = int(input(f"Guess a number (1-{max_number}): "))

    if guess < 1 or guess > max_number:
         print (
              f"This number is not part of the game. "
              f"Try again! You still have "
              f"{max_attempts - guesses} attempts left."
         )
         continue

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
