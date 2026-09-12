class Bank:

    def __init__(self, repository):
        self.repository = repository

    def save_account(self, account):
        self.repository.save(account)