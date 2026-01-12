import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"(http(s)?:\/\/)(www\.)?youtube.com\/embed(\/\w+)"

    match = re.search(pattern, s)
    if match:
        return f"{match.group(1)}youtu.be{match.group(4)}"
    else:
        return None


...

if __name__ == "__main__":
    main()
