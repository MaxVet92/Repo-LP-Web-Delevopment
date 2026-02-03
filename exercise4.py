import datetime
import uuid


class Transaction:
    def __init__(self, type_, amount, source_account=None, target_account=None, note=""):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.now()
        self.type = type_  # 'deposit', 'withdraw', 'transfer'
        self.amount = amount
        self.source_account = source_account
        self.target_account = target_account
        self.note = note

    def __repr__(self):
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

        if self.type == "deposit":
            return f"[{ts}] Deposit +${self.amount:.2f} ({self.note})"

        if self.type == "withdraw":
            return f"[{ts}] Withdraw -${self.amount:.2f} ({self.note})"

        if self.type == "transfer":
            return (
                f"[{ts}] Transfer -${self.amount:.2f} "
                f"from {self.source_account} to {self.target_account} ({self.note})"
            )

        return f"[{ts}] {self.type} ${self.amount:.2f} ({self.note})"


class Account:
    def __init__(self, owner_name, initial_balance=0.0):
        self.number = self._generate_account_number()
        self.owner = owner_name
        self._balance = float(initial_balance)
        self.transactions = []

    @staticmethod
    def _generate_account_number():
        # Short unique account number
        return str(uuid.uuid4())[:8]

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount
        tx = Transaction(
            type_="deposit",
            amount=amount,
            target_account=self.number,
            note=note
        )
        self.transactions.append(tx)
        return tx

    def withdraw(self, amount, note=""):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        tx = Transaction(
            type_="withdraw",
            amount=amount,
            source_account=self.number,
            note=note
        )
        self.transactions.append(tx)
        return tx

    def add_transaction(self, transaction):
        # Used for transfers
        self.transactions.append(transaction)


class Bank:
    def __init__(self, name="My Bank"):
        self.name = name
        self.accounts = {}  # account_number -> Account

    def create_account(self, owner_name, initial_balance=0.0):
        account = Account(owner_name, initial_balance)
        self.accounts[account.number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit(self, account_number, amount, note=""):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account.deposit(amount, note)

    def withdraw(self, account_number, amount, note=""):
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account.withdraw(amount, note)

    def transfer(self, source_number, target_number, amount, note=""):
        if source_number == target_number:
            raise ValueError("Cannot transfer to the same account.")

        source = self.get_account(source_number)
        target = self.get_account(target_number)

        if not source:
            raise ValueError("Source account not found.")
        if not target:
            raise ValueError("Target account not found.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > source.balance:
            raise ValueError("Insufficient funds in source account.")

        # Perform transfer
        source._balance -= amount
        target._balance += amount

        tx_out = Transaction(
            type_="transfer",
            amount=amount,
            source_account=source_number,
            target_account=target_number,
            note=note
        )

        tx_in = Transaction(
            type_="transfer",
            amount=amount,
            source_account=source_number,
            target_account=target_number,
            note=note
        )

        source.add_transaction(tx_out)
        target.add_transaction(tx_in)

        return tx_out

    def list_accounts(self):
        return list(self.accounts.values())


def prompt_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text).strip())
        except ValueError:
            print("Please enter a valid number.")


def main():
    bank = Bank("Example Bank")

    def print_menu():
        print("\n--- Example Bank ---")
        print("1) Create account")
        print("2) View account balance")
        print("3) Deposit")
        print("4) Withdraw")
        print("5) Transfer")
        print("6) Show transaction history")
        print("7) List accounts")
        print("0) Exit")

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Owner name: ").strip()
            initial = prompt_float("Initial deposit (0 if none): ")

            acc = bank.create_account(name, initial)
            print(
                f"Account created. Number: {acc.number}, "
                f"Owner: {acc.owner}, Balance: ${acc.balance:.2f}"
            )

        elif choice == "2":
            num = input("Account number: ").strip()
            acc = bank.get_account(num)

            if not acc:
                print("Account not found.")
            else:
                print(
                    f"Account {acc.number} - Owner: {acc.owner} "
                    f"- Balance: ${acc.balance:.2f}"
                )

        elif choice == "3":
            num = input("Account number: ").strip()
            amount = prompt_float("Amount to deposit: ")
            note = input("Note (optional): ").strip()

            try:
                tx = bank.deposit(num, amount, note)
                print("Deposit successful:", tx)
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            num = input("Account number: ").strip()
            amount = prompt_float("Amount to withdraw: ")
            note = input("Note (optional): ").strip()

            try:
                tx = bank.withdraw(num, amount, note)
                print("Withdrawal successful:", tx)
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            src = input("Source account number: ").strip()
            tgt = input("Target account number: ").strip()
            amount = prompt_float("Amount to transfer: ")
            note = input("Note (optional): ").strip()

            try:
                tx = bank.transfer(src, tgt, amount, note)
                print("Transfer successful:", tx)
            except Exception as e:
                print("Error:", e)

        elif choice == "6":
            num = input("Account number: ").strip()
            acc = bank.get_account(num)

            if not acc:
                print("Account not found.")
            elif not acc.transactions:
                print("No transactions for this account.")
            else:
                print(f"Transaction history for {acc.number}:")
                for t in acc.transactions:
                    print(" -", t)

        elif choice == "7":
            accounts = bank.list_accounts()
            if not accounts:
                print("No accounts.")
            else:
                print("Accounts:")
                for a in accounts:
                    print(f" - {a.number}: {a.owner} (${a.balance:.2f})")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please pick a valid option.")


if __name__ == "__main__":
    main()
