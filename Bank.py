class Application:
    def __init__(self):
        self.accounts = {}
        self.existingAccount = {}

    def showMainMenu(self, accountNumber="", initialBalance=0.0):
        self.accountNumber = accountNumber
        self.initialBalance = initialBalance

        while True:  # Loop to keep showing the main menu until exit
            print("\nMain Menu:")
            print("1. Select Account")
            print("2. Open Account")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                account_number = input("Enter Account Number: ")
                if account_number in self.accounts:
                    print(f"Account {account_number} selected")
                    self.existingAccount = self.accounts[account_number]

                    # Show account menu with placeholder methods
                    self.showAccountMenu(self.checkBalance, self.deposit, self.withdraw, self.exitAccount)
                else:
                    print("Account doesn't exist. Please try again.")

            elif choice == "2":
                account_number = input("Enter new account number: ")
                if account_number in self.accounts:
                    print("Account already exists.")
                else:
                    initial_balance = 0.0  # Default balance for new account
                    self.accounts[account_number] = {"Balance": initial_balance}
                    print(f"Account {account_number} opened with balance ${initial_balance: }")

            elif choice == "3":
                print("Exiting the application...")
                return  # Exit the main menu loop

            else:
                print("Invalid choice. Please try again.")

    def openAccount(self, accountNumber, initialBalance):
        # Open an account if it doesn't exist
        if accountNumber in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[accountNumber] = {"Balance": initialBalance}
            print(f"Account {accountNumber} opened with balance ${initialBalance: }")

    def showAccountMenu(self, checkBalance, deposit, withdraw, exitAccount):
        print("\nAccount Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit Account")

        option = input("Enter option: ")
        if option == "1":
            checkBalance()

        elif option == "2":
            deposit()

        elif option == "3":
            withdraw()

        elif option == "4":
            exitAccount()
            print("Exiting Account...")

    # Placeholder methods for account menu actions
    def checkBalance(self):
        if self.existingAccount:
            print(f"Current balance: ${self.existingAccount['Balance']: }")
        else:
            print("No account selected.")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if self.existingAccount:
            self.existingAccount["Balance"] += amount
            print(f"${amount} deposited. New balance: ${self.existingAccount['Balance']: }")
        else:
            print("No account selected.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.existingAccount:
            if self.existingAccount["Balance"] >= amount:
                self.existingAccount["Balance"] -= amount
                print(f"${amount} withdrawn. New balance: ${self.existingAccount['Balance']: }")
            else:
                print("Insufficient balance.")
        else:
            print("No account selected.")

    def exitAccount(self):
        self.existingAccount = {}

    def run(self):
        # Start the application by showing the main menu
        print("Welcome to the Account Management System")
        self.showMainMenu()


# To execute the program and display the main menu, create an instance of Application and call run()
app = Application()
app.run()
