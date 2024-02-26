class CheckingAccount:
    def __init__(self,accountNumber="",personFirstName="",personLastName="",balance=0.0):
        self._accountNumber=accountNumber
        self._personLastName=personLastName
        self._personFirstName=personFirstName
        self._balance=balance

    def getAccountNumber(self):
        return self._accountNumber
    def getPersonFirstName(self):
        return self._personFirstName
    def getPersonLastName(self):
        return self._personLastName
    def getBalance(self):
        return self._balance

    def withdraw(self,amount):
        if amount<=self._balance: #if the amount is less than or equal to the balance
            self._balance-=amount #adjust the balance, subtract the amount from the balance
            return True #return True=> the transaction was successful
        return False #return False=>the transaction failed because the amount is greater than the balance

    def deposit(self,amount):
        if amount>0: #if the amount is positive
            self._balance+=amount #add the amount to the balance
            return True #return True=> successful transaction
        return False #return fasle if the amount is 0 or negative, False=>failed transaction

class SavingsAccount(CheckingAccount):
    def __init__(self,accountNumber="",personFirstName="",personLastName="",balance=0.0,monthlyInterest=0.0,balanceLimit=0.0):
        super().__init__(accountNumber,personFirstName,personLastName,balance)
        self._monthlyInterest=monthlyInterest
        self._balanceLimit=balanceLimit

    def withdraw(self,amount):
        if self._balance-amount >= self._balanceLimit: #if it is within the balance limit
            return super().withdraw(amount) #call the parent function withdraw
        return False #Transaction failed because the user wants to withdraw beyond the balance limit
