#Set

def printSet():
    Set = {1.2,3, 'i', 'ii', 'iii'}
    print(type(Set))

def printAllSet():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    print(Set)

def AddNewEle():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    Set.add('iv')
    print(Set)

def AddOneEle():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    Set.add(1)
    print(Set)

def EmptySet():
    Set = set()
    ans1 = input("Set 1: ")
    ans2 = input("Set 2: ")
    ans3 = input("Set 3: ")
    Set.add(ans1)
    Set.add(ans2)
    Set.add(ans3)
    print(Set)

def EmptyUpdateSet():
    Set = set()
    ans1 = input("Set 1: ")
    ans2 = input("Set 2: ")
    ans3 = input("Set 3: ")
    Set.update(ans1)
    Set.update(ans2)
    Set.update(ans3)
    print(Set)

def DelIfromSet():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    Set.remove('i')
    print(Set)

def numberOfmember():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    print(len(Set))

def numberInSet():
    Set = {1,2,3, 'i', 'ii', 'iii'}
    ans = eval(input('Number: '))
    print(ans in Set)

def union():
    Set1, Set2 = {1,2,3,4,5},{3,4,5,6}
    print(Set1 | Set2)

def intersection():
    Set1, Set2 = {1,2,3,4,5},{3,4,5,6}
    print(Set1 & Set2)

def Minus():
    Set1, Set2 = {1,2,3,4,5},{3,4,5,6}
    print(Set1 - Set2)

def Minus2():
    Set1, Set2 = {1,2,3,4,5},{3,4,5,6}
    print(Set2 - Set1)

def symmetricDifference():
    Set1, Set2 = {1,2,3,4,5},{3,4,5,6}
    print(Set1 ^ Set2)

print(symmetricDifference())