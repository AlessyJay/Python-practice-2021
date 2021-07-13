while True:
    USD = eval(input("Please, insert your money in USD: "))
    THB = USD*32.5

    if USD <= 0:
        print("You don't have any money!!")
    elif USD >= 0:
        print(THB)