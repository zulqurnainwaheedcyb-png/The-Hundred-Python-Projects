# strings are immutable in python.
n = 'b!!!! harry!!! !!!!!!'
print(n.upper())
# the string is not changed but a new string is made.
print(len(n))
print(n.lower())
print(n.rstrip('!'))
print(n.replace('harry','jhon'))
print(n.split(" "))
# split into arrays.
print(n.capitalize())
# only converts first letter in upper case, others in lower case.
print(n.center(50))
# 50 means fifty spaces.
print(n.count('!'))
# count() counts the times of occurance of particular object in strings.
print(n.endswith("!!!"))
# endswith() tells either it is ending with that one or not,in True and False.
print(n.find("ha"))
print(n.isalnum())
# alnum() is alpha numeric means the string should be the alphabat and numbers not other characters so it will be true.
print(n.isprintable())
l = "       "
print(l.isspace())
print(n.istitle())
# only returns true if the first letter of string is captalize other wise false.
print(n.startswith("b!!"))
print(n.swapcase())