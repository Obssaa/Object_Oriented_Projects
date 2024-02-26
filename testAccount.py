from account import CheckingAccount,SavingsAccount

sav_1=SavingsAccount(accountNumber="12345",personFirstName="Ahmad",personLastName="Saed",
                     balance=float(input("enter the balance please")),monthlyInterest=0.01,balanceLimit=2000
                     )
sav_1.withdraw(500)
print("balance is",sav_1.getBalance()) #balance is: 2500
sav_1.withdraw(1000) # it will violate the 2000 balance limit because it would make the balance 1500
print("balance is",sav_1.getBalance()) #balance remains the same 2500