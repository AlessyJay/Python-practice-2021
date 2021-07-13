while True:
    ans = eval(input("Please, insert your number here (only positive int): "))
    num = ans**(1/2)

    if num%1 ==0:
        print("Yes, it's an integer!")
    else:
        print("No, it's not an integer!")