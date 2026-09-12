from Depositable import Depositable
from Withdrawable import Withdrawable


class ATM(Depositable, Withdrawable):

    def deposit(self, amount):
        print(f"Depositing Rs. {amount}")

    def withdraw(self, amount, entered_pin=None):
        print(f"Withdrawing Rs. {amount}")