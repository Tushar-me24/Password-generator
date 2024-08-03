import random
import string
pass_len = int(input("Enter the length of password: "))
password = ""
char = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
for i in range(pass_len):
    password += random.choice(char)
print(password)