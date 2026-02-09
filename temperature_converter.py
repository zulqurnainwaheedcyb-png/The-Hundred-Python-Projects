temp = float(input("enter the temperature : "))
unit = (input("C or F ? ")).upper()
if unit == "C":
    f = (temp*9/5)+32
    print(temp,"C = ",f,"F")
elif unit == "F":
    c = (temp-32)*9/5
    print(temp,"F = ",c,"C")
else:
    print("Invalid UNIT")