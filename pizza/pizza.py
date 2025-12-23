from tabulate import tabulate
import sys
import csv


def main():
    table = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)

        for row in reader:
            table.append(row)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
