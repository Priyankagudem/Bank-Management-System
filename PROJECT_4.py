class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def mini_statement(self):
        print(f"\n--- Mini Statement ---")
        print(f"Username: {self.username}")
        print(f"Balance: ₹{self.balance}")
        print("----------------------\n")


class BankManagement:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        username = input("Enter a new username: ")
        if username in self.accounts:
            print("Username already exists. Try another.")
            return
        password = input("Create a password: ")
        self.accounts[username] = Account(username, password)
        print("Account created successfully!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = self.accounts.get(username)

        if user and user.password == password:
            print(f"\nWelcome, {username}!")
            self.user_menu(user)
        else:
            print("Invalid username or password.")

    def user_menu(self, user):
        while True:
            print("\n--- User Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Mini Statement")
            print("5. Log Out")

            choice = input("Choose an option (1-5): ")

            if choice == '1':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                except ValueError:
                    print("Invalid amount.")

            elif choice == '2':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")

            elif choice == '3':
                user.check_balance()

            elif choice == '4':
                user.mini_statement()

            elif choice == '5':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")


def main():
    bank = BankManagement()

    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            bank.create_account()
        elif choice == '2':
            bank.login()
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
