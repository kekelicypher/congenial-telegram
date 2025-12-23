import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")


def main():
    students = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {}
                last, first = row["name"].rstrip().split(", ")
                student["first"] = first
                student["last"] = last
                student["house"] = row["house"]
                students.append(student)
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
