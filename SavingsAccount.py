from BankAccount import BankAccount
from Depositable import Depositable
from Withdrawable import Withdrawable
from Transferable import Transferable
from StatementProvider import StatementProvider


class SavingsAccount(
    BankAccount,
    Depositable,
    Withdrawable,
    Transferable,
    StatementProvider
):

    def __init__(self, account_number, name, age, balance):
        super().__init__(
            account_number,
            name,
            age,
            balance,
            "Savings"
        )

    def transfer(self, amount):
        print(f"Transferring Rs. {amount}")

    def print_statement(self):
        print(
            f"Statement for Account #{self.get_account_number()}"
        )

        for entry in self.transaction_log:
            print(entry)

        print(f"Current Balance: Rs. {self.get_balance()}")