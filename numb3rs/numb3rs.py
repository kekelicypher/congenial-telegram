import re
import sys

# if len(sys.argv) < 2:
#     pass
# else:
#     ip = sys.argv[1]


def main():
    # print(validate(ip))
    # sys.exit()
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # single = r"([0-9]\.){3}([0-9])"
    # double = r"([0-9][0-9]\.){3}([0-9][0-9])"
    # triple = r"([0-2][0-5][0-5])\.{3}([0-2][0-5][0-5])"
    final = r"((([0-9]\.){3}([0-9])$)|(([0-9][0-9]\.){3}([0-9][0-9])$)|(([0-2][0-5][0-5]\.){3}([0-2][0-5][0-5]))$)"

    # if re.search(r"(([0-2][0-5][0-5])|([0-9])|([0-9][0-9])\.){3}(([0-2][0-5][0-5])|([0-9])|([0-9][0-9]))", ip):
    if re.search((final), ip):
        return True
    else:
        return False


...

if __name__ == "__main__":
    main()
