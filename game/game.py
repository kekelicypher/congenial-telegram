import random


def main():
    while True:
        try:
            num = int(input("Level: "))
            if num > 0:
                break
        except ValueError:
            pass

    computer_guess = random.randint(1, num)

    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess > 0:
                break
        except ValueError:
            pass

    while guess != computer_guess:
        if guess < computer_guess:
            print("Too small!")

        elif guess > computer_guess:
            print("Too high!")

        guess = int(input("Guess the number: "))

    print("Just right!")


if __name__ == "__main__":
    main()
