import random

cpu = random.randint(1,100)
chances = 5
game = True
while game:
    guess = int(input("Enter your guess : "))

    if cpu == guess:
        print("Congratulations, You have guessed the number")
        game = False
        break
    elif cpu > guess:
        print("You have guessed smaller number")
    elif cpu < guess:
        print("You have guessed greater number")
    else:
        print("You have guessed a wrong number")

    chances -= 1
    if chances == 0:
        print(f"You lose the game. Number was {cpu}")
        break
