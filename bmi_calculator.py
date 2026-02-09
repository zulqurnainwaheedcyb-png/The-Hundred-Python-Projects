weight = float(input("enter the weight: "))
height = float(input("enter the height: "))

bmi = weight/height**2

print("The BMI is : ",round(bmi,2))
# round(bmi,2) used to round off two decimal places.