import random as r

char = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-,./';?><ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = int(input("enter the length : "))
password = ""
for a in range(length):
    password+=r.choice(char)
print("your password is : ",password)    