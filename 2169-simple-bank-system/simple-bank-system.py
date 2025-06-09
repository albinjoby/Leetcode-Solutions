from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 <= account1-1 < self.size and 0 <= account2-1 < self.size and self.balance[account1-1] >= money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account-1 < self.size:
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account-1 < self.size and self.balance[account-1] >= money:
            self.balance[account-1] -= money
            return True
        return False