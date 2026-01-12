def main() -> None:
    items: dict = {}

    while True:
        try:
            item: str = input("").upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

        except EOFError:
            print()
            break

    for key, value in sorted(items.items()):
        print(value, key)


if __name__ == "__main__":
    main()
