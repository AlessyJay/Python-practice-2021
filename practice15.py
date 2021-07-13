ans = eval(input("Please, insert your number here: "))

if ans == 0:
    print("zero")
elif ans > 0:
    if ans%2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif ans <0:
    if ans%2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")