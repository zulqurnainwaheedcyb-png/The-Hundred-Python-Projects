year = int(input("Enter the year : "))

if (year%4==0 & year%100!=0)|(year%400==0):
    print("It is Leap Year")
else:
    print("It is not leap year")