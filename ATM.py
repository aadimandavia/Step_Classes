from BankService import BankService


class ATM(BankService):

    def deposit(self, amount):
        print(f"Depositing Rs. {amount}")

    def withdraw(self, amount):
        print(f"Withdrawing Rs. {amount}")

    # ATM does not need transfer functionality
    def transfer(self, amount):
        print("Not used by ATM")

    # ATM does not print bank statements
    def print_statement(self):
        print("Not used by ATM")

    # ATM does not handle loan applications
    def apply_for_loan(self):
        print("Not used by ATM")