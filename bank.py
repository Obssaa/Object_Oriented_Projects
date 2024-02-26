from bank_account import BankAccount

class Bank:
    def __init__(self):
        self.__accounts=[]

    def findAccount(self,accountNumber):
        for account in self.__accounts:
            if account.getAccountNumber()==accountNumber:
                return account
        return None

    def addAccount(self,accountNumber,firstName,lastName,balance):
        try:
            if self.findAccount(accountNumber)==None:
                account=BankAccount(accountNumber,firstName,lastName,balance)
                self.__accounts.append(account)
            else:
                print("Sorry. An account with the same number already exists")
        except:
            print("Sorry. We couldn't create the account. Check that the balance is 0 or more AED")

    def deleteAccount(self,accountNumber):
        account=self.findAccount(accountNumber)
        if account==None:
            print("Sorry. This account does not exist")
        else:
            self.__accounts.remove(account)
    def transfer(self,fromAccountNumber,toAccountNumber,amount):
        fromAccount=self.findAccount(fromAccountNumber)
        toAccount=self.findAccount(toAccountNumber)
        if fromAccount==None or toAccountNumber==None:
            print("One of the accounts does not exist")
        else:
            try:
                fromAccount.withdraw(amount)
                toAccount.deposit(amount)
            except:
                print("Sorry. We cannot perform the transfer maybe because (1) there are no sufficient funds in the first account, (2) the transfer amount is zero or below")

FAB=Bank()
FAB.addAccount("1","Ahmed","Said",10000)
FAB.addAccount("2","Nouf","Ali",5000)
FAB.transfer("1","2",500)
print("done")