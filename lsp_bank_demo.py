from BankAccount import BankAccount
from FixedDepositAccount import FixedDepositAccount


def test_withdraw(account):
    print(
        f"Trying to withdraw from {account.get_account_type()} account..."
    )

    account.withdraw(1000, 1234)

    print("Withdrawal successful")


savings_account = BankAccount(
    101,
    "Ravi",
    22,
    5000,
    "Savings"
)

fixed_deposit_account = FixedDepositAccount(
    102,
    "Aadi",
    22,
    10000,
    "Fixed Deposit"
)

accounts = [
    savings_account,
    fixed_deposit_account
]

for account in accounts:
    test_withdraw(account)