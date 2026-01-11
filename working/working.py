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
            elif int(hour) == 12:
                hour = 0
        else:
            hour = time.split(" ")[0]
            if int(hour) < 12:
                hour = int(hour) + 12
                minute = 0
            elif int(hour) == 12:
                hour = 0
    elif "AM" in time:
        if ":" in time:
            time2 = time.split(" ")[0]
            hour, minute = time2.split(":")
            hour = int(hour)
            minute = int(minute)
        else:
            hour = int(time.split(" ")[0])
            minute = 0

    # if hour > 23 or  minute > 60:
    #     raise ValueError

    return f"{hour:02}:{minute:02}"


def convert(s):
    # pattern = r"([0-9])|(1[0-2])[:/s]/sto/s([0-9])|(1[0-2])/s(PM|AM)"
    # pattern = r"^[0-9]|1[0-2][:/s][0-5][0-9]?$"
    # pattern = r"[0-9] (AM|PM) to [0-9] (AM|PM)"
    pattern = r"((?P<first>([0-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)) (to) (?P<second>([0-9]|1[0-2])(:([0-5][0-9]))? (AM|PM)))"

    match = re.match(pattern, s)

    if match:

        first, second = match.group("first", "second")
        # if match.group(7) != "to":
        #     raise ValueError
        first = convert_to_24h(first)
        second = convert_to_24h(second)

        return f"{first} to {second}"
    else:
        raise ValueError


try:
    print(convert(sys.argv[1]))
    sys.exit()
except IndexError:
    pass

if __name__ == "__main__":
    main()
