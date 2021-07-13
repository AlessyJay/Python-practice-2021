shopping = eval(input("Shopping: "))
hour = eval(input("Hour: "))
minute = eval(input("Minute: "))
SH = (hour-3)*40
SM = 40

if shopping >= 1000:
    if SH+SM >= 160:
        print("Your parking fee is ", SH+SM, "THB, do you want to pay one price at once? It'll cost 150THB.")
    elif hour <= 3:
        print("Your parking fee is free!")
    elif hour > 3 and minute == 0:
        print("Your parking fee is ", SH, "THB")
    elif hour > 3 and minute/60 != 0:
        print("Your parking fee is ", ((hour-3)*40)+SM, "THB")
    elif hour < 0 and minute < 0:
        print("It can't be negative!")
elif shopping < 1000:
    if ((hour-1)*40)+SH >= 160:
        print("Your parking fee is ", SH+SM, "THB, do you want to pay one price at once? It'll cost 150THB.")
    elif hour <= 1 and minute/60 != 0:
        print("Your parking fee is free!")
    elif hour > 1 and minute/60 != 0:
        print("Your parking fee is ", ((hour-1)*40)+SM, "THB")
    elif hour < 0 and minute < 0:
        print("It can't be negative!")