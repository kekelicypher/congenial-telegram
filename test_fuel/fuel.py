def main():
    fraction = input("Fraction: ")
    fraction = convert(fraction)

    print(gauge(fraction))


def convert(fraction):
    while True:
        try:
            num1, num2 = fraction.split('/')

            if (num1.isdigit()):
                raise ValueError

            num1 = int(num1)
            num2 = int(num2)


            answer = (num1 / num2) * 100
            answer = round(answer)
            return answer
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
