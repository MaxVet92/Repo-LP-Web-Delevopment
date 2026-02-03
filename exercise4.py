import datetime
import random
import string


class Account:
    def __init__(self, owner, balance=0):
        self.iban = self.generate_iban()
        self.owner = owner
        self.balance = float(balance)
        self.transactions = []

        if balance > 0:
            self.add_transaction("deposit", balance, note="Initial deposit")

    def generate_iban(self, country_code="DE49", digit_count=18):
        digits = ''.join(random.choices(string.digits, k=digit_count))
        return f"{country_code}{digits}"

    def add_transaction(self, transaction_type, amount, note="", source_account=None, target_account=None):
        self.transactions.append({
            "time": datetime.datetime.now(),
            "type": transaction_type,
            "amount": amount,
            "source": source_account,
            "target": target_account,
            "note": note
        })

    def deposit(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.add_transaction("deposit", amount, note=note)

    def withdraw(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.add_transaction("withdraw", amount, note=note)

    def transfer_to(self, target_account, amount, note=""):
        if amount <= 0:
            raise ValueError("Transfer must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        target_account.balance += amount

        self.add_transaction(
            "transfer-out",
            amount,
            note=note,
            source_account=self.iban,
            target_account=target_account.iban
        )

        target_account.add_transaction(
            "transfer-in",
            amount,
            note=note,
            source_account=self.iban,
            target_account=target_account.iban
        )


class Bank:
    def __init__(self, name="Blabla Bank"):
        self.name = name
        self.accounts = {}

    def create_account(self, owner, balance=0.0):
        account = Account(owner, balance)
        self.accounts[account.iban] = account
        return account

    def get_account(self, iban):
        return self.accounts.get(iban)

    def list_accounts(self):
        return self.accounts.values()


def main():
    bank = Bank()

    while True:
        print("\n--- Blabla Bank ---")
        print("1) Create account")
        print("2) Balance")
        print("3) Deposit")
        print("4) Withdraw")
        print("5) Transfer")
        print("6) Transactions")
        print("0) Exit")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                owner_name = input("Owner name: ")
                initial_balance = float(input("Initial balance: "))
                account = bank.create_account(owner_name, initial_balance)
                print(f"Account created: {account.iban}")

            elif choice == "2":
                account = bank.get_account(input("Account number: "))
                print(f"Balance: ${account.balance:.2f}")

            elif choice == "3":
                account = bank.get_account(input("Account number: "))
                amount = float(input("Amount: "))
                account.deposit(amount)
                print("Deposit successful")

            elif choice == "4":
                account = bank.get_account(input("Account number: "))
                amount = float(input("Amount: "))
                account.withdraw(amount)
                print("Withdrawal successful")

            elif choice == "5":
                source_account = bank.get_account(input("Source account: "))
                target_account = bank.get_account(input("Target account: "))
                amount = float(input("Amount: "))
                source_account.transfer_to(target_account, amount)
                print("Transfer successful")

            elif choice == "6":
                account = bank.get_account(input("Account number: "))
                for transaction in account.transactions:
                    print(transaction)

            elif choice == "0":
                break

            else:
                print("Invalid option")

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
