from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    try:
        date_of_birth = input("Enter date of birth: ")    
        print(convert(date_of_birth))
    except Exception:
        sys.exit("Invalid date")


def convert(date_of_birth):

    date_of_birth = date.fromisoformat(date_of_birth)
    age = date.today() - date_of_birth
    age_in_minutes = age.days*24*60
    return f'{p.number_to_words(age_in_minutes).replace("and ", "")} minutes'





if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(convert(sys.argv[1]))
        sys.exit()
    main()
