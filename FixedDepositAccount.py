from BankAccount import BankAccount


class FixedDepositAccount(BankAccount):

    def withdraw(self, amount, entered_pin=None):
        raise UnsupportedOperationException(
            "Fixed Deposit Account does not allow withdrawals"
        )


class UnsupportedOperationException(Exception):
    pass