def convert(words):
    words = words.replace(':)', '🙂').replace(':(', '🙁')
    return words

def main():
    answer = input("Enter some words: ")
    print(convert(answer))

main()
