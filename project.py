#ADETAYO ABIODUN AYODELE
#07083420729
#An ATM program

#here is where the user enters his/her PIN
pin = int(input("Please enter your PIN: "))
#if the PIN matches, it proceeds to this
if (pin == 1234):
    print("PIN OK!, please proceed")      
    print (" 1. Balance \n 2. Withdraw \n 3. Fund transfer \n 4. Quick teller \n 5. Quit \n")
    transaction = float(input("Please choose a transaction \n"))
    balance = 100000
    if (transaction == 1):
        print ("Dear customer, your balance is N", balance)
    if (transaction ==2 ):
        print ("Choose an amount \n 1. 500 \n 2. 1,000 \n 3. 2,000 \n 4. 5,000 \n 6. 10,000 \n 7. 20,000 \n")
        withdraw = float(input("Please enter the amount to withdraw: "))
        if (balance > withdraw):
            print ("Please take your cash")
        elif (withdraw > balance):
            print ("Insufficient funds")
    if (transaction == 3):
        print ("Please wait...")
        transfer = float(input("Please enter the amount to transfer: "))
        transFer = float(input("Please enter the account number: "))
        if (balance > transfer):
            print ("Transfer successful, thank you for banking with us")
        elif(balance < transfer):
            print("Insufficient fund")
    if (transaction == 4):
        print ("Quick teller can't function nowdue to network problem, please try again later \n")

    if (transaction == 5):
        print ("Thank you for banking with us")
    else:
        print ()
#this occurs if the user enters a wrong password
else:
    print ("PIN incorrect")
