#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 

class BankAccount:
  def __init__ (self,__accountNumber,__accountHolderName,__initialBalance=0):
    self.__acccountNumber=__accountNumber
    self.__accountHolder=__accountHolderName
    self.__AccountBalance=__initialBalance
    
  def depositMoney(self,amount):
    self.__AccountBalance +=amount
    print("Rs.",amount," has been deposited in your account.")
    
  def withdrawMoney(self,amount):
   if amount>self.__AccountBalance:
     print("insufficient Balance")
   else:
    self.__AccountBalance -=amount
    print("Rs.",amount," has beenwithdrawn from your account")

  def checkBalance(self):
    print("current balance: ",self.__AccountBalance)

obj=BankAccount(2838203938,"karthika")
obj.depositMoney(5000)
obj.withdrawMoney(2000)
obj.checkBalance()