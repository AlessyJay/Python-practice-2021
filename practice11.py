while True:
    ans = eval(input("Christ's Year: "))
    buddhaYear = ans+543
    
    if ans >= 0:
        print(buddhaYear)
    elif ans < 0:
        print("Pleae, insert the year more than or equal to 0!")