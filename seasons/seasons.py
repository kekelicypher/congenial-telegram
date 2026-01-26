from datetime import date


def main():
    date_of_birth = input("Enter date of birth: ")
    date.fromisocalendar(date_of_birth)
    print(date_of_birth)
    print(convert(date_of_birth))


def convert(date):
    ...

if __name__ == "__main__":
    main()
