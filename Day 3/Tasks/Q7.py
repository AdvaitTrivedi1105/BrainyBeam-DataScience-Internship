# Q-7  ATM program with deposit, balance check and withdraw using class.

class ATM():
    bal = 1000
    def balance(self):
        return self.bal
    def deposit(self, amount):
        self.bal += amount
        return self.bal
    def withdraw(self, amount):
        if (amount > self.bal):
            return "Insufficient balance, cannot withdraw"
        self.bal -= amount
        return self.bal


# Main - Driver Code
atm = ATM()

while True:
    print("\n1) Check Balance")
    print("2) Deposit Amount")
    print("3) Withdraw Amount")
    print("4) Exit\n")

    choice = int(input("\nEnter your choice: "))
    
    if (choice==1):
        print(f"\nAccount Balance: {atm.balance()}")
    elif (choice==2):
        amount = int(input("\nEnter amount to deposit: "))
        print(f"\nDeposit Amount: {amount}")
        print(f"Account Balance: {atm.deposit(amount)}")
    elif (choice==3):
        amount = int(input("Enter amount to withdraw: "))
        print(f"\nWithdraw Amount: {amount}")
        print(f"Account Balance: {atm.withdraw(amount)}")
    elif (choice==4):
        exit()
    else:
        print("\nPlease enter valid choice !!!")