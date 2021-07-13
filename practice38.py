def first():
    #จงเขียนโปรแกรมรับ input 1 ตัวและให้หาค่าเงินบาทเป็นดอลล่า

    ans = input("Your currency (T/U): ").upper()
    if ans == "T":
        USD()
    elif ans == "U":
        THB()

def USD():
    while True:
        thb = eval(input("Please, input your THB: "))
        total = thb / 32

        if thb == 0:
            print("You don't have money!")
        else:
            print("You have ", total, " USD")

def THB():
    while True:
        usd = eval(input("Please, input your THB: "))
        total = usd * 0.032

        if usd == 0:
            print("You don't have money!")
        else:
            print("You have ", total, " USD")

print(first())