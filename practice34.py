def typeAndLength():
    tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
    print(len(tuple1), '\n', type(tuple1))

def bringIndex1():
    tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
    print(tuple1[1])

def bringIndexM2():
    tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
    print(tuple1[-2])

def bringChina():
    tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
    print(tuple1[2])

def bringEgypt():
    tuple1 = ('America', 'Brazil', 'China', 'Dominican', 'Egypt')
    print(tuple1[-1])

def bringIdx1to3():
    tuple1 = ('One', 'Two', 'Three', 1,2,3)
    print(tuple1[1:4])

def bring2toM2():
    tuple1 = ('One', 'Two', 'Three', 1,2,3)
    print(tuple1[2:-1])

def bringThreeAnd1():
    tuple1 = ('One', 'Two', 'Three', 1,2,3)
    print(tuple1[2:4])

def OneTwoThree():
    tuple1 = ('One', 'Two', 'Three', 1,2,3)
    print(tuple1[0:3])

def NumOneTwoThree():
    tuple1 = ('One', 'Two', 'Three', 1,2,3)
    print(tuple1[3:6])
    
def LengthFinder():
    tuple1 = ('one', 'two', 'three', 'four', 'five')
    print(len(tuple1))

def memberInTuple():
    tuple1 = ('one', 'two', 'three', 'four', 'five')
    ans = input('Your word: ')
    print(ans in tuple1)

print(memberInTuple())
