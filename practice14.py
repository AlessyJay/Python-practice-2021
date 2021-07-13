while True:     
    THB = eval(input("Please, in sert your amount in THB: "))
    USD = THB/32.80
    Bank = USD*0.30

    if THB <= 0:
        print("You don't have any money!!")
        break
    elif THB >= 0:
        print("You can exchange in USD: ", USD)
        print("The bank will gain: ", Bank)
    
