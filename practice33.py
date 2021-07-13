def del1():
    list1 = [1,2,3,1,2,3]
    del list1[1]
    print(list1)

def delAll3():
    list1 = [1,2,3,1,2,3]
    del list1[2]
    del list1[-1]
    print(list1)

def remove1():
    list1 = [1,2,3,1,2,3]
    list1.remove(1)
    list1.remove(1)
    print(list1)

def removeAll():
    list1 = [1,2,3,1,2,3]
    list1.clear()
    print(list1)

def lengthFinder():
    list1 = [1,2,3,'a','b','c']
    print(len(list1))

def member():
    list1 = [1,2,3,4,5]
    ans = eval(input("Nubmer: "))
    print(ans in list1)

print(member())