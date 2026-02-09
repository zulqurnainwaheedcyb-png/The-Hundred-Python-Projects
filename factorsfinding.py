num = int(input("Enter the number : "))
print("The factors of ",num,"are : ")
# we wrote (1,num+1) because it will check the possibility from
# 1 to that number so we set range to that number 1 ahead.
for i in range(1,num+1): 
    if num % i== 0:
        print(i)