from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator
from SavingsInterestPolicy import SavingsInterestPolicy
from CurrentInterestPolicy import CurrentInterestPolicy


def main():
    account = BankAccount(
        101,
        "Ravi",
        17,
        200,
        "Savings"
    )

    account.set_pin(1234)

    account.deposit(1000)
    account.withdraw(500, 1234)

    # Wrong PIN, should fail
    account.withdraw(500, 9999)

    repository = AccountRepository()
    repository.save(account)

    notification_service = NotificationService()
    notification_service.send(
        f"Account {account.get_account_number()} updated successfully."
    )

    statement_generator = StatementGenerator()
    statement = statement_generator.generate(account)
    print(statement)

    # Interest calculation now uses a policy
    savings_policy = SavingsInterestPolicy()

    interest = savings_policy.calculate(
        account.get_balance()
    )

    print(
        "Interest earned: Rs. "
        + str(interest)
    )

    # Example of Current account interest policy
    current_policy = CurrentInterestPolicy()

    print(
        "Current account interest on Rs. 10000: Rs. "
        + str(current_policy.calculate(10000))
    )


if __name__ == "__main__":
    main()