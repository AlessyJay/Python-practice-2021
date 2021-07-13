num1 = eval(input("Number 1: "))
num2 = eval(input("Number 2: "))
ans = num1+num2

if ans > 0 :
    print("a + b > 0 :", ans)
elif ans < 0:
    print("a + b < 0 :", ans)
elif ans == 0 :
    print("a + b = 0 :", ans)