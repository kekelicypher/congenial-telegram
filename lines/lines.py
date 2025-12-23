import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")


def main():
    print(line_counter())


def line_counter():
    count = 0
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith("#") or line.isspace():
                    continue

                count += 1
            return count

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
