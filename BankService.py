from abc import ABC, abstractmethod


class BankService(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

    @abstractmethod
    def print_statement(self):
        pass

    @abstractmethod
    def apply_for_loan(self):
        pass