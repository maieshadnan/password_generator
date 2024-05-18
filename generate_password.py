import sys
import string
import random

# python3 generate_password.py [PASSWORD_LENGTH] [SITE] (Optional)

alphabets = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits
punctuation_symbols = string.punctuation

all = alphabets + numbers + punctuation_symbols

password = ""

newline = "\n"

for i in range(0, int(sys.argv[1])):
    password += random.choice(all)

password_file = open("passwords.txt", "a")

if len(sys.argv) >= 3:
    password_file.write(sys.argv[2] + ":" + password + newline)
else:
    password_file.write("unknown" + ":" + password + newline)

password_file.close()

print("Generated Password is " + password)
