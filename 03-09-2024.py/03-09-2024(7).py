'''7.Write a program that computes the net amount of a bank account based a transaction 
log from console input.The transaction log format is shown as following: D 100 W 200 D 
means deposit while W means withdrawal. Suppose the following input is supplied to the
program: D 300 D 300 W 200 D 100 Then, the output should be: 500'''

total = 0
while True:
    deposit_withdraw_transac = input()
    if deposit_withdraw_transac == "":
        break
    else:
        deposit_withdraw_transac = deposit_withdraw_transac.split(" ")
        if deposit_withdraw_transac[0] == "D":
            total = total + int(deposit_withdraw_transac[1])
        elif deposit_withdraw_transac[0] == "W":
            total = total - int(deposit_withdraw_transac[1])
print(total)