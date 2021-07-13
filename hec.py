def SumTheLoop(): 
    x = 0
    print("Before: ", x)

    for i in [3,5,7,9,12,14,16,18,20]:
        x = x + i
        print("Loop: ", x, i)
    print("Solution: ", x)

def FindingTheAverage():
    x = 0
    count = 0
    print("Before: ", x, count)

    for i in [3,5,7,9,12,14,16,18,20]:
        count += 1
        x = x+i
        print("Loop: ", count, x)
    print("Solution: ", count, x, (x/count))

def Filtering():
    num1 = [3,5,7,9,12,14,16,18,20]
    print("Before: ", num1)
    for i in num1:
        if i > 10:
            print(i)

def Boolean():
    num1 = False
    x = [3,5,7,9,12,14,16,18,20]

    print("Before: ", num1)
    for i in x:
        if num1 == 14:
            num1 = True
        print(num1, i)
    print("After: ", num1)

print(Boolean())