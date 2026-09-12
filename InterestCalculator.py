class InterestCalculator:

    def calculate_interest(self, balance, account_type):
        # This implementation violates OCP because every new
        # account type requires modifying this method.

        if account_type == "Savings":
            return balance * 0.04

        elif account_type == "Current":
            return balance * 0.01

        else:
            return 0.0


# If we add a 4th account type, for example "Salary",
# we would have to modify this method.
#
# Changes required:
# 1. Add another elif condition for "Salary".
# 2. Add the new interest rate.
# 3. Modify the existing InterestCalculator code.
#
# If more account types are added, this method keeps growing.
# Therefore, the class is not closed for modification.