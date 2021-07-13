while True: 
    s = eval(input("Shopping (THB): "))
    h = eval(input("Hour: "))
    m = eval(input("Minute: "))
    SH = (h-4)*30
    SM = 30

    if s >= 1000:
        if h <= 4 and m >= 0:
            print("Your parking fee is free!")
        elif h > 4 and m == 0:
            print("Your parking fee is ", SH, "THB")
        elif h > 4 and m/60 != 0:
            print("Your parking fee is ", SH+SM, "THB")
        elif h < 0 and m < 0:
            print("It can't be negative!")
    elif s < 1000:
        if h > 1:
            print("Your parking fee is ", ((h-1)*30)+SM, "THB")
        elif h > 1 and m/60 != 0:
            print("Your parking fee is ", ((h-1)*30)+SM, "THB")
        elif h <= 1 and h >= 0 and m > 0 and m <= 60:
            print("Your parking fee is free!")
        elif h < 0 and m < 0:
            print("It can't be negative!")