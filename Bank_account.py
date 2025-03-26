class BankAccount:
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance  # Changed from intial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited ETB{amount:.2f}. New balance: ETB{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ETB{amount:.2f}. New balance: ETB{self.balance:.2f}")
        else:
            print("Insufficient balance! Please make another transaction.")

    def display_balance(self) -> None:
        print(f"Account balance for {self.holder_name}: ETB{self.balance:.2f}")

    def __str__(self) -> str:
        return f"BankAccount(account_number={self.account_number}, holder={self.holder_name}, balance=ETB{self.balance:.2f})"


if __name__ == "__main__":
    account = BankAccount("10006699*****", "Miss Yordanos Tesfaye", 3000.0)
    account.deposit(1200.0)
    account.withdraw(800.0)
    account.display_balance()
    print(account)
