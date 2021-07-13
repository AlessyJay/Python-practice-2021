import random

def money():
    THB = eval(input("Please, insert your amount: "))
    USD = THB/32.80

    if THB > 0:
        bank = USD * 0.30
        print("he amount you'll get in USD is", USD, "and the bank will get", bank, "THB")
    elif THB <= 0:
        print("You don't have any money.") 

def num10():
    while True:
        num1 = eval(input("Number 1: "))
        num2 = eval(input("Number 2: "))

        if num1 == num2:
            print("same amount")
        else:
            if num1 > num2:
                print(num1)
            else:
                print(num2)

def num11():
    string1 = input("String 1: ")
    string2 = input("String 2: ")

    if len(string1) == len(string2):
        print("Same length")
    else:
        if len(string1) > len(string2):
            print("Not same, string 1 has", len(string1) - len(string2), "letters more than string 2!")
        else:
            print("Not same, string 2 has", len(string2) - len(string1), "letters more than string 1!")

def num12():
    num1 = int(input("Number 1: "))

    if num1 % 3 == 0:
        print("It can be moded by 3")
    else:
        print("It can't be moded by 3!")

def num13():
    num1 = eval(input("Number 1: "))

    if (num1 % 3 == 0) and (num1 % 5 == 0):
        print("It can be moded by 3 and 5")
    else:
        print("It can't be moded by 3 and 5")

def num15():
    num1 = eval(input("Number 1: "))
    num2 = eval(input("Number 2: "))
    num3 = eval(input("Number 3: "))

    if num1 + num2 > num3:
        print("a + b > c")
    else:
        print("c is greater than a and b")

def num16():
    while True:
        hour = eval(input("Hour: "))
        minute = eval(input("Minute: "))
        H = (hour - 1) * 30

        if hour <= 1:
            print("Your parking fee is free.")
        elif hour > 1 and minute != 0:
            print("Your parking fee is", H + 30, "THB")
        elif hour > 1 and minute == 0:
            print("Your parking fee is", H, "THB")

def num17():
    while True:
        hour = eval(input("Hour: "))
        minute = eval(input("Minute: "))
        H = (hour - 1) * 30

        
        if hour < 0 and minute < 0:
            print("Please, positive number only!")
        elif hour <= 1:
            print("Your parking fee is free.")
        elif hour > 1 and minute != 0:
            print("Your parking fee is", H + 30, "THB")
        elif hour > 1 and minute == 0:
            print("Your parking fee is", H, "THB")
        elif hour < 0 and minute < 0:
            print("Please, positive number only!")

def num18():
    while True:
        bill = eval(input("Your bill: "))
        hour = eval(input("Your hour: "))
        minute = eval(input("Your minute: "))
        H4 = (hour - 4) * 30
        H1 = (hour - 1) * 30

        if bill >= 1000:
            if hour <= 4 and minute == 0:
                print("Your parking fee is", H4, "THB")
            elif hour >= 4 and minute != 0:
                print("Your parking fee is", H4 + 30, "THB")
        elif bill < 1000:
            if minute != 0:
                print("Your parking fee is", H1 + 30, "THB")
            else:
                print("Your parking fee is", H1, "THB")

def num19():
    bill = eval(input("Your bill: "))

    if bill >= 1000:
        discount = bill * 0.1
        print("You need to pay", (bill - discount), "THB, you get", discount, "or 10 percent off!")
    elif bill >= 10000:
        discount = bill * 0.15
        print("You need to pay", (bill - discount), "THB, you get", discount, "or 15 percent off!")
    elif bill >= 50000:
        discount = bill * 0.2
        print("You need to pay", (bill - discount), "THB, you get", discount, "or 20 percent off!")
    else:
        print("You need to pay", bill)

def num20():
    gender = input("Gender (M/F): ").upper()
    weight = eval(input("Weight(kg): "))
    height = eval(input("Height(cm): "))

    if gender == "M":
        if weight > (height - 100):
            print("You should do exercise!")
        else:
            print("You are quite fit!")
    elif gender == "F":
        if weight > (height - 110):
            print("You should do exercise!")
        else:
            print("You are quite fit!")
 
def num21():
    vel = eval(input("Velocity: "))

    if vel > 120:
        print("Catch that rabbit!!")
    else:
        print("It's OK, don't worry about this one")

def num22():
    vel = eval(input("Velocity: "))

    if vel > 120:
        print("Your fine is $1000!")
    elif vel > 80 and vel <= 120:
        print("Your fine is $500")
    else:
        print("It's OK, don't worry about this one")

def num23():
    time = eval(input("Time: "))

    if time >= 4:
        print("It's dangerous for your ears!")
    else:
        print("Enjoy!")

def num24():
    status = input("Status (clear/average/busy): ").lower()
    distance = eval(input("Distance: "))

    if status == "clear":
        print("Travelling fee is", (distance * 10))
    elif status == "average":
        print("Travelling fee is", (distance * 12))
    elif status == "busy":
        print("Travelling fee is", (distance * 15))

def num25():
    score = eval(input("Score: "))

    if score >= 50:
        print("Pass!")
    else:
        print("Fail!")

def num26():
    score = eval(input("Score: "))

    if score >= 50 and score < 60:
        print("D")
    elif score >= 60 and score < 70:
        print("C")
    elif score >= 70 and score < 80:
        print("B")
    elif score >= 80:
        print("A")
    else:
        print("Fail")

def num27():
    isMember = input("Member: ").upper()
    bill = eval(input("Bill: "))

    if isMember == "YES":
        if bill >= 500:
            discount = bill * 0.05
            print("You need to pay", bill - discount, "THB, you'll get", discount, "THB discount!")
        elif bill >= 1000:
            discount = bill * 0.1
            print("You need to pay", bill - discount, "THB, you'll get", discount, "THB discount!")
        elif bill >= 5000:
            discount = bill * 0.15
            print("You need to pay", bill - discount, "THB, you'll get", discount, "THB discount!")
        else:
            print("You need to pay", bill, "THB")
    elif isMember == "NO":
        print("You need to pay", bill, "THB")

def num28():
    currency = input("Currency: ").upper()
    amount = eval(input("Amount: "))

    if currency == "USD":
        THB = amount * 32.5
        print("You'll get", THB, "THB")
    elif currency == "JYP":
        THB = amount * 0.29
        print("You'll get", THB, "THB")

def num29():
    order = input("Order: ").upper()
    amount = eval(input("Amount: "))

    if order == "FRIED EGG":
        egg = amount * 7
        print(egg, "THB")
    elif order == "OMELET":
        egg = amount * 10
        print(egg, "THB")
    elif order == "BOIL EGG":
        egg = amount * 5
        print(egg, "THB")

def num30():
    order = input("Order: ").upper()

    if order == "FRIED EGG":
        print("We suggest you to order with TomJood")
    elif order == "OMELET":
        print("We suggest you to order with Kai Look Kaeoy")
    elif order == "BOIL EGG":
        print("We suggest you to order with Yam Kai Daw")
    print("Our store also has fried egg, omelet, and boiled egg")

print(num30())

