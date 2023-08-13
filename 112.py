from random import randint


def main():
    number = randint(1, 10)
    chances = 5

    print("Welcome to number guessing game")

    while chances > 0:
        print(f"You have {chances} chances left")
        guess = input("Guess the number : ")
        try:
            guess = int(guess)

            if guess == number:
                print("You won!")
                break
            elif guess > number:
                print("Try smaller than", guess)
            else:
                print("Try bigger than", guess)
            chances -= 1
        except ValueError:
            print("Entry must be a number. Try again")
    if chances == 0:
        print("Game over! The number was", number)

    if input("Play again ? (y/n) : ") == "y":
        main()

main()