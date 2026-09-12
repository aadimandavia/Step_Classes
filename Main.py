from BankAccount import BankAccount
from FileAccountRepository import FileAccountRepository
from Bank import Bank


def main():

    account = BankAccount(
        101,
        "Ravi",
        22,
        5000,
        "Savings"
    )

    account.deposit(1000)

    # Swap repository implementation here
    repository = FileAccountRepository()

    bank = Bank(repository)

    bank.save_account(account)


if __name__ == "__main__":
    main()