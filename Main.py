from BankAccount import BankAccount
from AccountRepository import AccountRepository
from NotificationService import NotificationService
from StatementGenerator import StatementGenerator

from SavingsInterestPolicy import SavingsInterestPolicy
from CurrentInterestPolicy import CurrentInterestPolicy
from SalaryAccount import SalaryAccount
from SalaryInterestPolicy import SalaryInterestPolicy


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

    # Savings interest
    savings_policy = SavingsInterestPolicy()
    print(
        "Savings interest: Rs. "
        + str(savings_policy.calculate(account.get_balance()))
    )

    # Current interest
    current_policy = CurrentInterestPolicy()
    print(
        "Current interest on Rs. 10000: Rs. "
        + str(current_policy.calculate(10000))
    )

    # New Salary account
    salary_account = SalaryAccount(
        102,
        "Aadi",
        22,
        10000
    )

    salary_policy = SalaryInterestPolicy()

    print(
        "Salary interest: Rs. "
        + str(salary_policy.calculate(salary_account.get_balance()))
    )


if __name__ == "__main__":
    main()