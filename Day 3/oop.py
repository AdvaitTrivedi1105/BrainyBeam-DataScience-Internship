class ATM():
    b=1000
    def balance(self):
        return self.b
    def deposit(self,amount):
        self.b += amount
        return self.b
    def withdraw(self,amount):
        if amount > self.b:
            return "Insufficient Balance"
        self.b -= amount
        return self.b

obj = ATM()

while True:
    print("\n1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Quit")

    choice = int(input("Enter choice: "))
    if (choice == 1):
        print("\nBalance: ",obj.balance())
    elif (choice == 2):
        amount = int(input("Enter amount to deposit: "))
        print("\nBalance: ",obj.deposit(amount))
    elif (choice == 3):
        amount = int(input("Enter amount to withdraw: "))
        print("\nWithdraw: ",obj.withdraw(amount))
    elif (choice == 4):
        exit()