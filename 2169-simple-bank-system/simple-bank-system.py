class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.size = len(balance)
        self.lock = [False] * self.size

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 <= account1-1 < self.size and 0 <= account2-1 < self.size and self.balance[account1-1] >= money:
            if not self.lock[account1-1] and not self.lock[account2-2]:
                self.lock[account1-1] = True
                self.lock[account2-1] = True
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                self.lock[account1-1] = False
                self.lock[account2-1] = False
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account-1 < self.size:
            if not self.lock[account-1]:
                self.lock[account-1] = True
                self.balance[account-1] += money
                self.lock[account-1] = False
                return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account-1 < self.size and self.balance[account-1] >= money:
            if not self.lock[account-1]:
                self.lock[account-1] = True
                self.balance[account-1] -= money
                self.lock[account-1] = False
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)