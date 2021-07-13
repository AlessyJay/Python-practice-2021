import random
import math
import sys

r = random.randint(0, 20)

while True:
    ans = eval(input("Please, guess your number: "))
    if ans < r:
        print("Too bad, try raising your number next time. :)")
    elif ans > r:
        print("Too bad, try lowering your number next time. :)")
    elif ans == r:
        print("Congrats!")
        break

ques = input("Do you want to play again? (Y / N): ")
if ques == "N" or "n":
    sys.exit