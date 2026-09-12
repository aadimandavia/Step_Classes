from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from FixedDepositAccount import FixedDepositAccount
from Withdrawable import Withdrawable


savings_account = SavingsAccount(
    101,
    "Ravi",
    22,
    5000
)

current_account = CurrentAccount(
    102,
    "Aadi",
    22,
    5000
)

fixed_deposit_account = FixedDepositAccount(
    103,
    "Rahul",
    22,
    10000
)


# Only accounts that are actually withdrawable
# are placed in this list.
accounts = [
    savings_account,
    current_account
]


for account in accounts:
    print(
        f"Withdrawing from {account.get_account_type()} account..."
    )

    account.set_pin(1234)

    if account.withdraw(1000, 1234):
        print("Withdrawal successful")


print("\nFixed Deposit account is not included because")
print("it does not support withdrawal.")