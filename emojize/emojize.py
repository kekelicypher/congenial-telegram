import emoji



def main()->None:
    user_input:str = input("Input: ")
    print("Output: " + emoji.emojize(user_input, language = 'alias'))




if __name__ == "__main__":
    main()
