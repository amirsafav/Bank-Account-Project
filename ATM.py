option = None

from Account import *
def diplayMenu():
    print(
    """\n    Welcome to CIS-1400 Bank
        Please selection an option from the list below
        1. Display Current Accounts
        2. Make a Deposit
        3. Make a Withdraw
        4. Add Account
        5. Remove Account
        6. Quit\n
    """)
    global option
    option = int(input("Enter your selection (1-6)"))
    while option < 1 or option > 6:
        option = int(input("Enter your selection (1-6)"))

def makeDeposit(b:Bank):
    accNum = int(input("Enter an account number to deposit into: "))
    account = b.findAccount(accNum)
    tryAgain = True
    while account == None and tryAgain:
        print("Invalid account number, would you like to try again (Y/N)")
        response = input().upper()
        while response != 'Y' and response != 'N':
            response = input("Invalid response, would you like to try again (Y/N)")
        if response == "N":
            tryAgain = False
        else:
            accNum = int(input("Enter an account number to deposit into: "))
            account = b.findAccount(accNum)
    if account != None:
        amount = float(input("Deposit Amount: "))
        account.deposit(amount)

def makeWithdraw(b:Bank):
    accNum = int(input("Enter an account number to withdraw from: "))
    account = b.findAccount(accNum)
    tryAgain = True
    while account == None and tryAgain:
        print("Invalid account number, would you like to try again (Y/N)")
        response = input().upper()
        while response != 'Y' and response != 'N':
            response = input("Invalid response, would you like to try again (Y/N)")
        if response == "N":
            tryAgain = False
        else:
            accNum = int(input("Enter an account number to withdraw fro : "))
            account = b.findAccount(accNum)
    if account != None:
        amount = float(input("Withdraw Amount: "))
        if account.withdraw(amount):
            print("Please take your ${}".format(amount))
        else:
            print("Insufficient funds")

def addAccount(b:Bank):
    checking = input("Is this a checking account (Y/N): ").upper()
    while checking != "Y" and checking != "N":
        checking = input("Is this a checking account (Y/N)").upper()
    if checking == "Y":
        b.addAccount(True)
    else:
        b.addAccount(False)

def removeAccount(b:Bank):
    accNum = int(input("Enter an account number to remove: "))
    acc = b.findAccount(accNum)
    if acc != None:
        print("Are you sure you want to remove the following account (Y/N): ")
        print(acc.displayAccount())
        confirm = input().upper()
        while confirm != "Y" and confirm != "N":
            confirm = input("Remove this account (Y/N): ").upper()
        if confirm == "Y":
            b.removeAccount(acc.getAccountNumber())
    else:
        print("Account number not found")

def save(b:Bank):
    response = input("Would you like to save (Y/N): ").upper()
    while response != "Y" and response != "N":
        response = input("Would you like to save (Y/N): ")
    if response == "Y":
        b.writeToFile()


def main():
    b = Bank()
    while option != 6:
        diplayMenu()
        if option == 1:
            b.displayAccounts()
        if option == 2:
            makeDeposit(b)
        if option == 3:
            makeWithdraw(b)
        if option == 4:
            addAccount(b)
        if option == 5:
            removeAccount(b)
        if option == 6:
            save(b)



if __name__ == '__main__':
    main()


