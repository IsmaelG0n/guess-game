import random

#adicionar a escolha de dificuldade antes de iniciar o game.
while True:
    difficulty = input("Easy, Medium or Hard?: ").lower()

    if difficulty in ["easy", "medium", "hard"]:
        break

    print ("Invalid options. Please choose Easy, Medium or Hard.")

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

    try: #validar que o input não seja uma letra ou um número decimal, apenas inteiro positivo.
        guess = int(input(f"Guess a number (1-{max_number}): "))

    except ValueError:
        print("Please enter a valid number.")

        continue

    if guess < 1 or guess > max_number: # Se o numero for menor ou maior que o limite do jogo, ele não conta como tentativa e o jogador é avisado.
         print (
              f"This number is not part of the game. "
              f"Try again! You still have "
              f"{max_attempts - guesses} attempts left."
         )
         continue

    guesses += 1 # contador de tentativas

    difference = abs(secret - guess) # diferença entre o palpite e o número secreto

    if guess != secret: # garante que o feedback é dado apenas quando o jogador erra o palpite.

        if difference <= 5:
            print ("Very hot!")

        elif difference <= 10:
            print ("Warm!")

        else:
            print ("Cold!")
    
    if guess < secret:
        print("Too low")

    elif guess > secret:
        print("Too high")

    else:

        score = 110 - (guesses * 10) # pontuação baseada no número de tentativas
        print(f"Got it in {guesses} guesses")
        print(f"Your score is {score} points.")

        break

else:
    print(f"You've used all {max_attempts} guesses. The secret number was {secret}.")
