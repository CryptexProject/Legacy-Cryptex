import random
import pyperclip as pc
from mods.clearScreen import clear_screen as cs
from mods.menu import passlogo
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

cs()
print(passlogo)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

passwordList = []

for char in range(1, nr_letters + 1):
  passwordList += random.choice(letters)

for char in range(1, nr_symbols + 1):
  passwordList += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  passwordList += random.choice(numbers)

random.shuffle(passwordList)
password = ""
for char in passwordList:
  password += char
print(f"\nYour new password is: \n\n{password}")
pc.copy(password)
input("\nYour new password has been copied to the clipboard \nPress Enter to go to main menu")
cs()
