def F():
    while True:
        ans = eval(input("Please, insert your temperature in F: "))
        celsius = (ans - 32) *5/9

        if ans < 32:
            print("Too cold to live!")
        elif ans >= 32:
            print(celsius)

def C():
    while True:
        ans = eval(input("Please, insert your temperature in C: "))
        fahrenheit = (ans * 9/5) +32

        if ans < 0:
            print("Too cold to live!")
        elif ans >= 0:
            print(fahrenheit)

ask = input("Please, choose Fahrenheit or Celsius to calculate (F/C). ")
if ask == "C":
    print(C())
elif ask == "F":
    print(F())