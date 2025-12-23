import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        first = generate_interger(level)
        second = generate_interger(level)
        wrongs = 0

        while True:
            answer = int(input(f"{first} + {second} = "))
            correct = first + second

            if answer == correct:
                score += 1
                break
            else:
                print("EEE")
                wrongs += 1
                if wrongs == 3:
                    print(f"{first} + {second} = {correct}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_interger(level):
    if level == 1:
        number = random.randint(1, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)

    return number


if __name__ == "__main__":
    main()
