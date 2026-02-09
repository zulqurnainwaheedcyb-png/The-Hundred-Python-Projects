current_year = 2026
birth_year = int (input("enter your birth year : "))
if(birth_year > current_year):
    print("You are not born YET !")
else:    
    age = current_year - birth_year
    print("your age is : ",age)