#Let´s generate passwords

import random
import string

LETTERS = string.ascii_letters
NUMBERS = '0123456789'
SPECIAL = "-+*%&#$!_"

SYMBOLS = LETTERS + NUMBERS + SPECIAL

print("Lets generate a password")
len = int(input(" Enter password lenght:"))

password = "".join(random.sample(SYMBOLS, len))

print("Your password is: ", password)