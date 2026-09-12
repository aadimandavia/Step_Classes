class BankAccount:

    """
    Reasons for BankAccount to change:

    1. Account operation changes
       - Changes to deposit(), withdraw(), close_account(),
         reopen_account(), PIN handling, etc.

    2. Validation changes
       - Changes to age validation.
       - Changes to minimum balance rules.

    3. Database changes
       - Changes if MySQL is replaced with another database.
       - Changes if the database saving mechanism changes.

    4. Notification changes
       - Changes if the email provider changes.
       - Changes if email is replaced by SMS or another notification system.

    5. Interest calculation changes
       - Changes when interest rates change.
       - Changes when new account types are introduced.

    6. Statement changes
       - Changes if the format of the bank statement changes.
       - Changes if new transaction information needs to be displayed.

    Therefore, BankAccount has multiple responsibilities
    and multiple reasons to change, which violates SRP.
    """

    def __init__(self, account_number, name, age, balance, account_type):