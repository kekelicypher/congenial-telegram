def main():
    userInput = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    userInput = userInput.strip().lower()
    if userInput in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")


main()
