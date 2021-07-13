#คำนวนหาค่าจอดรถ โดยให้ user ใส่ 2 input

while True:
    hour = eval(input("Hour: "))
    minute = eval(input("Minute: "))

    hour = hour * 30
    Min = 1*30

    if hour == 0 and Min < 60:
        print("Your parking fee is: ", "0", "$")
    elif hour > 1 and Min > 0:
        print("Your parking fee is: ", hour+Min, "$")
    elif hour < 0 and minute < 0:
        print("Please, insert time correctly!")