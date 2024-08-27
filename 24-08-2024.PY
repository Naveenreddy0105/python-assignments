print ("welcome to ATM")
print("Banking")
Balance=1000
print("1.check Balance")
print("2.deposit")
print("3.withdraw")
print("4.exit")
option=True
option= int(input("Please enter your option (1-4): "))

if option==1:
    print("your current balance is :{balance}")
elif option==2:
    deposit=float(input("enter the amount to deposit:"))
if deposit > 0:
    Balance +=deposit
    print("you have deposit your new balance is :")
else:
    print ("invalid deposit amount")
if option==3:
    withdraw=float(input("enter the amount to withdraw"))
if withdraw<= Balance:
    Balance-=withdraw
    print("you have withdrwa your new balance is :")
else :
    print ("invalid amount or insufficient funds.")

