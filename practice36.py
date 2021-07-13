#Dictionary

def FindType():
    key = {'first_name':'John', 'second_name':'Doe'}
    print(type(key))

def FirstValue():
    key = {'first_name':'John', 'second_name':'Doe'}
    print(key['first_name'])

def LastValue():
    key = {'first_name':'John', 'second_name':'Doe'}
    print(key['second_name'])

def AllKey():
    key = {'first_name':'John', 'second_name':'Doe'}
    print(key.keys())

def AllValues():
    key = {'first_name':'John', 'second_name':'Doe'}
    print(key.values())

def ChangeValue():
    key = {'first_name':'John', 'second_name':'Doe'}
    key['first_name'] = 'Jane'
    print(key)

def AddNewValue():
    key = {'first_name':'John', 'second_name':'Doe'}
    key['Age'] = [32]
    print(key)

def AddNewValues():
    key = {'first_name':'John', 'second_name':'Doe'}
    key.update({'Age':'32', 'Hobby':{'Coding','Studying'}})
    print(key)

def EmptyDic():
    key = {}
    ans1 = (input("Your key: "))
    ans2 = (input("Your value: "))
    key[ans1] = [ans2]
    print(key)

def DeleteDictValue():
    key = {'first_name':'John', 'second_name':'Doe', 'Age':'32'}
    del key['Age']
    print(key)

def DelAll():
    key = {'first_name':'John', 'second_name':'Doe', 'Age':'32'}
    key.clear()
    print(key)

def numberOfKey():
    key = {'first_name':'John', 'second_name':'Doe', 'Age':'32'}
    print(len(key.keys()))

def memberInDict():
    while True:
        key = {'first_name':'John', 'second_name':'Doe', 'Age':'32'}
        ans = input("Your Key: ")
        print(ans in key)

def memberInDictValue():
    while True:
        key = {'first_name':'John', 'second_name':'Doe', 'Age':'32'}
        ans = input("Your Value: ")
        print(ans in key.values())

print(memberInDictValue())