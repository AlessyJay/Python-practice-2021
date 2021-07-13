num1 = eval(input("Number 1: "))
num2 = eval(input("Number 2: "))
ans = num1+num2

if ans > 0:
    if ans%2 == 0:
        print("Positive Even")
    else:
        print("postive Odd")
elif ans < 0:
    if ans%2 == 0:
        print("Negative Even")
    else:
        print("negative Odd")
elif ans == 0:
    print("Zero")
