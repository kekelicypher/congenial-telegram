import sys
import re


def main():
    print(convert(input("Hours: ")))


def convert_to_24h(time):
    if "PM" in time:
        if ":" in time:
            time2 = time.split(" ")[0]
            hour, minute = time2.split(":")
            if int(hour) < 12:
                hour = int(hour) + 12
        else:
            hour = time.split(" ")[0]
            if int(hour) < 12:
                hour = int(hour) + 12
            minute = "00"
    elif "AM" in time:
        if ":" in time:
            time2 = time.split(" ")[0]
            hour, minute = time2.split(":")
        else:
            hour = time.split(" ")[0]
            minute = "00"
        if int(hour) == 12:
            hour = "00"

    return f"{hour}:{minute}"


def convert(s):
    # pattern = r"([0-9])|(1[0-2])[:/s]/sto/s([0-9])|(1[0-2])/s(PM|AM)"
    # pattern = r"^[0-9]|1[0-2][:/s][0-5][0-9]?$"
    # pattern = r"[0-9] (AM|PM) to [0-9] (AM|PM)"
    pattern = r"((?P<first>([0-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)) to (?P<second>([0-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)))"

    match = re.match(pattern, s)

    if match:
        # print(match.groups())
        first, second = match.group("first", "second")
        first = convert_to_24h(first)
        second = convert_to_24h(second)

        return f"{first} to {second}"
    else:
        print("There is no match")
        return False


if __name__ == "__main__":
    main()
