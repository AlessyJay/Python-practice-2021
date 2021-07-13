#Create a random number for the input, if number is even say "true!", but if the number is odd say "false!"

import random
import os
import sys
import math

n = random.randint(0,20)

if n%2 == 0:
    print("true")
else:
    print("false")