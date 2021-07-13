def shop():
    shopping = eval(input("Shopping: "))
    hour = eval(input("Hour: "))
    minute = eval(input("Minute: "))
    h = ((hour-3)*30)
    m = 40

    if h+m >= 160:
        print("Your parking fee is ", h+m, "THB, do you want to pay one time for 150THB?")
    elif hour <= 3 and minute/60 != 0:
        print("Your parking is free!")
    elif hour > 3 and minute/60 != 0:
        print("Your parking fee is ", h+m, "THB")

def noShop():
    hour = eval(input("Hour: "))
    minute = eval(input("Minute: "))
    h = ((hour-1)*30)
    m = 40

    if h+m >= 160:
        print("Your parking fee is ", h+m, "THB, do you want to pay one time for 150THB?")
    elif hour < 1 and minute/60 != 0:
        print("Your parking is free!")
    elif hour > 1 and minute/60 != 0:
        print("Your parking fee is ", h+m, "THB")

while True:
    ans = input("Are you willing to buy?: ")
    if ans == "yes":
        print(shop())
    elif ans == "no":
        print(noShop())