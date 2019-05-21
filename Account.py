
import pickle, shelve

class Account(object):
    nextAccountNumber = 13245
    def __init__(self, name,balance):
        self.__accountNumber = Account.nextAccountNumber
        self.__name = name
        self.__balance = balance
        Account.nextAccountNumber +1

    def getaccountNumber(self):
        numberOfAccount = self.__accountNumber
        return numberOfAccount
    def getName(self):
        Name = self.__name
        return Name
    def getBalance(self):
        Balance = self.__balance
        return Balance

    def deposit(self,amount):
        self.__balance += amount


    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return False

    def displayAccount(self):
        x =  "Name: " + str(self.__name) + '\nAcount Number: ' + str(self.__accountNumber) + "\nBalacnce:"+str(self.__balance )
        return x


class CheckingAccount(Account):
    interestRate = 0.0125

    minimumBalance = 500.00
    def __init__(self, name, balance):
        super(CheckingAccount,self).__init__(name, balance)

    def withdraw(self,amount,):

        if self.getBalance() >= amount:
            super().withdraw(amount)
            if self.getBalance() <= CheckingAccount.minimumBalance:
                super().withdraw(10)
            return True
        else:
            return False

    def depositInterest(self):
        intersetEarned = self.getBalance() * CheckingAccount.interestRate
        intersetEarned = round(intersetEarned,2)
        super.deposit(intersetEarned)

    def displayAccount(self):
        x = "Name: " + str(self.getName()) + '\nAccount Number: ' + str(self.getaccountNumber()) + "\nBalance:" +str(self.getBalance()) + "\nInterest Rate:" + str(self.interestRate* 100)
        return x


class Bank(object):

    def __init__(self):
        self.accounts = self.__generateAccounts()

    def __generateAccounts(self):
        accounts = open("BankAccountFile.dat", "rb")
        try:
            reading = pickle.load(accounts)
            accounts.close()
            return reading
        except:
            return []

    def writeToFile(self):
        f = open("BankAccountFile.dat", "wb")
        pickle.dump(f)
        f.close()
    def addAccount(self, checking:bool):
        name = input("Please input name:  ")
        balance = input("Please input Your balance")
        if checking == True:
            newAccount = CheckingAccount(name,balance)
        else:
            newAccount = Account(name,balance)
            newAccount = self.writeToFile()

    def findAccont(self,number):
        for account in self.accounts:
            if account.getaccountNumber() == number:
                return account
        return None
    def removeAccount(self,number):
        if number == self.accounts:
            self.accounts = []
            return True
        else:
            return False
    def displayAccounts(self):
        #numberOfAccounts = len(self.accounts)
        #for i in range(numberOfAccounts):
            #pass
        print(self.__generateAccounts())




def main():
    # s = CheckingAccount("Amir",500)
    # print(s.displayAccount())
    # s.deposit(5000)
    # print(s.withdraw(1000))
    # print(s.displayAccount())
    # print(s.withdraw(1000))
    A = Bank()
    print(A.displayAccounts())
    print(A.findAccont(12345))

if __name__=='__main__':
    main()




