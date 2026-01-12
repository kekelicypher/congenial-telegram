months: list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main() -> None:
    while True:
        try:
            month, day, year = get_date()
            break
        except TypeError:
            pass
    print(f"{year:}-{month:02}-{day:02}")


def get_date() -> list:
    while True:
        date: str = input("Date: ")
        if "/" in date:
            return f_format(date)
        elif " " in date:
            return s_format(date)
        else:
            pass


def s_format(date: str) -> list:
    try:
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
        day = int(day.removesuffix(","))
        year = int(year)
        if (month <= 12) and (day <= 31):
            return [month, day, year]
        else:
            pass
    except ValueError:
        pass


def f_format(date: str) -> list:
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if (month <= 12) and (day <= 31):
            return [month, day, year]
        else:
            pass
    except ValueError:
        pass


if __name__ == "__main__":
    main()
