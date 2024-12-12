import random
print("Welcome to Random password Generated")
randomchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz1234567890!@#$%^&"
numofpwd = int(input("Enter the number of password to be generated:"))
pwdleng = int(input("Enter the password length:"))
print("Hellow here your random passwords")
for i in range(numofpwd):
    pwd = ""
    for char in range(pwdleng):
        pwd = pwd + random.choice(randomchar)
    print(pwd)