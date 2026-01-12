def main():
    amount_due = 50
    print(f"Amount due: {amount_due}")
    amount = validate_money(int(input("Insert coin: ")))
    total = amount
    amount_due -= amount

    while amount_due != 0:
        print(f"Amount due: {amount_due}")
        amount = validate_money(int(input("Insert coin: ")))
        total += amount
        amount_due -= amount
        if amount_due < 0:
            break

    print(f"Change Owed: {total - 50 }")


def validate_money(money):
    if money in [25, 10, 5]:
        return money
    else:
        return 0


main()
