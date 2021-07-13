import math 
import random

level = random.randint(0, 9999)

def simp():
    tier = ""
    book = ""

    if level <500:
        tier = "Noob tier"
    elif level >= 500 and level <= 1000:
        tier = "Normal tier"
    elif level > 1000 and level < 4000:
        tier = "Simp tier"
    elif level > 4000 and level < 8999:
        tier = "Extra simp tier"
    elif level > 8999 and level < 9999:
        tier = "BookGamer"

    print("This is bookgamer's simp level: ", level, "Tier: ", tier)

simp()