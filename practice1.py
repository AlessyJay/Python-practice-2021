myFile = open("myFile.txt", "r")
Lime = myFile.readline()
while Lime:
    print(Lime)
    Lime = myFile.readline()
myFile.close()