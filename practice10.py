while True:
    ans = eval(input("Please, put your number here: "))
    if ans < 0:
        print("Please, insert the number that's greater than or equal to 0.")
    elif ans >= 0 and ans < 50:
        print("You got a F grade.")
    elif ans >= 50 and ans < 60:
        print("D")
    elif ans >= 60 and ans < 70:
        print("C")
    elif ans >= 70 and ans < 80:
        print("B")
    elif ans >= 80 and ans <= 100:
        print("A")
    elif ans > 100:
        print("There are no higher grades than A!")
    