def askUser():
    ans = str(input("Type: "))
    tier = {
        'A':'[80,100]',
        'B':'[70,80)',
        'C':'[60,70)',
        'D':'[50,60)',
        'F':'[0,50)'
    }
    
    for i in tier.keys():
        if ans.upper() == i:
            print("Here's the grade: ", tier[i])
    
askUser()