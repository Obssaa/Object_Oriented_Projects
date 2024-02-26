class BankAccount:
    def __init__(self,accountNumber="",firstName="",lastName="",balance=0.0):
        assert balance>=0
        self.__accountNumber=accountNumber
        self.__firstName=firstName
        self.__lastName=lastName
        self.__balance=balance

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getBalance(self):
        return self.__balance
    def getAccountNumber(self):
        return self.__accountNumber

    def setFirstName(self,firstName):
        self.__firstName=firstName
    def setLastName(self,lastName):
        self.__lastName=lastName

    def withdraw(self,amount):
        assert amount<=self.__balance
        self.__balance-=amount
    def deposit(self,amount):
        assert amount>0
        self.__balance+=amount

