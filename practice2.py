#BMI and BMR calculator
import sys
from tkinter import *

answer = input("What do you want to calculate?(BMI/BMR): ")
if answer == "BMI" or "bmi":
    BMI_calculator()
    

root = Tk()
root.withdraw()

def BMI_calculator():
    nameBMI = input("What's your name? ")
    weightBMI = eval(input("What's your weight? "))
    heightBMI = eval(input("What's your height? "))
    totalBMI = (weightBMI/heightBMI/heightBMI)*10000
    print(nameBMI, ": Your total BMI is: ", totalBMI)

def BMR_calculator():
    nameBMR = input("What's your name? ")
    genderBMR = input("What's your gender?(m/f): ")
    ageBMR = eval(input("What's your age? "))
    weightBMR = eval(input("What's your weight(kg)? "))
    heightBMR = eval(input("What's your height(cm)? "))
    
    if genderBMR == "m":
        totalBMRMale = (66.47 + (13.75 * weightBMR) + (5.003 * heightBMR) - (6.755 * ageBMR))
    elif genderBMR == "f":
        totalBMRFemale = (655.1 + (9.563 * weightBMR) + (1.85 * heightBMR) - (4.676 * ageBMR))