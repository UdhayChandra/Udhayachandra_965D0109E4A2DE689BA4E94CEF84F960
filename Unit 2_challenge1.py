class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount > self.__account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Create an instance of the BankAccount class
account1 = BankAccount("1234567890", "udhaya chandra", 1000.0)

# Test deposit and withdrawal functionality
account1.display_balance()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()
