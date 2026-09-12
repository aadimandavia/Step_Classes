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

        # Validation logic
        if age < 18:
            print("Age was below 18, correcting to 18")
            age = 18

        minimum_balance = 500.0 if account_type == "Savings" else 1000.0

        if balance < minimum_balance:
            print(
                f"Initial balance below minimum, correcting to {minimum_balance}"
            )
            balance = minimum_balance

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = "Active"

        self.pin = None

        self.transaction_log = []

    # ----------------------------------------------------
    # Account operations
    # ----------------------------------------------------

    def deposit(self, amount):

        if self.status != "Active":
            print("Account is not active")
            return False

        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount

        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def withdraw(self, amount, entered_pin):

        if self.status != "Active":
            print("Account is not active")
            return False

        if self.pin is not None:

            if entered_pin is None or entered_pin != self.pin:
                print("Incorrect PIN")
                return False

        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        minimum_balance = (
            500.0 if self.account_type == "Savings" else 1000.0
        )

        if self.balance - amount < minimum_balance:
            print("Withdrawal would breach minimum balance")
            return False

        self.balance -= amount

        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def close_account(self):

        if self.status == "Inactive":
            return False

        self.status = "Inactive"

        return True

    def reopen_account(self):

        if self.status == "Active":
            return False

        self.status = "Active"

        return True

    def set_pin(self, new_pin):

        if 1000 <= new_pin <= 9999:
            self.pin = new_pin
            return True

        return False

    def verify_pin(self, entered_pin):

        return self.pin is not None and self.pin == entered_pin

    # ----------------------------------------------------
    # Interest calculation
    # ----------------------------------------------------

    def calculate_interest(self):

        if self.account_type == "Savings":
            return self.balance * 0.04

        elif self.account_type == "Current":
            return self.balance * 0.01

        else:
            return 0.0

    # ----------------------------------------------------
    # Getters
    # ----------------------------------------------------

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def get_account_type(self):
        return self.account_type

    def has_pin(self):
        return self.pin is not None