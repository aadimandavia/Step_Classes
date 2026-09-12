from AccountRepository import AccountRepository


class FileAccountRepository(AccountRepository):

    def __init__(self, filename="accounts.txt"):
        self.filename = filename

    def save(self, account):
        with open(self.filename, "a") as file:
            file.write(
                f"{account.get_account_number()},"
                f"{account.get_name()},"
                f"{account.get_balance()}\n"
            )

        print("Account saved to file")

    def read_accounts(self):
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []
        