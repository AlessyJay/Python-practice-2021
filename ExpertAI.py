import sys
from tkinter import *

def read_file():
    with open('myFile.txt', 'r') as file:
        for line in file:
            country, capital = line.split("/")
            country = country.capitalize()
            capital = capital.capitalize()
            world_capital[country] = capital

def write_file(country_name, capital_name):
    with open('myFile.txt', 'a') as file:
        write_file('\n')
        file.write(country_name + '/' + capital_name)
        file.close()

message = Tk()
message.withdraw()
world_capital = {}
while True:
    read_file()
    simpledialog.askstring
    query_country = ""
    query_capital = simpledialog.askstring("Country", "Ask me the country: ")
    query_country = query_country.capitalize()

