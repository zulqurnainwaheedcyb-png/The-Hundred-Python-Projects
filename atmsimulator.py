balance = 100000
print("1.Check Balance.")
print("2.Withdraw Money")
choice = int(input("enter the choice: "))
if(choice == 1):
    print("your balance is : ",balance)
elif(choice==2):
    amount = int(input("enter the amount: "))
    if(amount<balance):
        print("Money withdrawed,Remaining balance is : ",balance-amount)
    else:
        print("Insufficient Balance")    