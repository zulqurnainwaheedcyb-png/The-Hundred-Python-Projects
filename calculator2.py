num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("enter operation to be done: ")
operation=input(" ")
if(operation=="+"):
    print("the answer is: ",num1 + num2)
elif(operation=="-"):
    print("the answer is : ",num1 - num2)
elif(operation=="*"):
    print("the answer is: ",num1 * num2) 
elif(operation=="/"):
    print("the answer is: ",float(num1/num2))
elif(operation=="%"):
    print("the answer is: ",num1%num2)      
else:
    print("Invalid operation selected")
