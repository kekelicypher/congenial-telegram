def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if first(s) and second(s) and third(s) and fourth(s):
        return True
    else:
        return False


def first(a):
    if a[:2].isalpha():
        return True
    else:
        return False


def second(b):
    if len(b) >= 2 and len(b) <= 6:
        return True
    else:
        return False


def third(c):
    number = False
    for i in c:
        if i.isdigit():
            if number == False and i == "0":
                return False
            number = True
        if i.isalpha() and number == True:
            return False
    return True


def fourth(d):
    letters = [",", ".", ",", "!", "?"]
    for i in d:
        if i in letters:
            return False
    return True


main()
