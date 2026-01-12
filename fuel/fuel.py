def main():

    while True:
        try:
            fraction = input("Fraction: ")
            num1, num2 = fraction.split("/")
            num1 = int(num1)
            num2 = int(num2)
            answer = convert(num1, num2)
            break
        except (ValueError, ZeroDivisionError):
            pass

    if answer <= 1:
        print("E")
    elif answer >= 99:
        print("F")
    else:
        print(f"{answer}%")


def convert(num1, num2):
    if (num1 > num2) or (num2 == 0) or (num1 < 0) or (num2 < 0):
        raise ValueError

    answer = (num1 / num2) * 100
    answer = round(answer)
    return answer


if __name__ == "__main__":
    main()
