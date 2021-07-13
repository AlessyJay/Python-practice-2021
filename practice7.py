def vowel(ans, vow):
    if ans in vow:
        print("There are vowel in English!")
    else:
        print("There are no vowel!")

while True:
    ans = input("Vowel: ")
    vowel(ans, vow = ["a","e","i","o","u"])