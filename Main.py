from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService


def main():

    account = BankAccount(
        101,
        "Ravi",
        17,
        200,
        "Savings"
    )

    # Age corrected to 18
    # Balance corrected to 500

    account.set_pin(1234)

    # -----------------------------
    # Account operations
    # -----------------------------

    account.deposit(1000)

    account.withdraw(500, 1234)

    # Wrong PIN, should fail
    account.withdraw(500, 9999)

    # -----------------------------
    # Repository
    # -----------------------------

    repository = AccountRepository()
    repository.save(account)

    # -----------------------------
    # Notification
    # -----------------------------

    notification_service = NotificationService()

    notification_service.send(
        f"Account {account.get_account_number()} "
        f"updated successfully."
    )

    # Interest is still here for now.
    # It will be refactored in Section 2.

    print(
        "Interest earned: Rs. "
        + str(account.calculate_interest())
    )


if __name__ == "__main__":
    main()