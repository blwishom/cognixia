
class User():
    def __init__(self, username, password, account_number):
        self.username = username
        self.password = password
        self.account_number = account_number

    def dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'account': self.account_number
        }

class Bank():
    def __init__(self, deposit, withdrawal):
        self.deposit = deposit
        self.withdrawal = withdrawal

    def dict(self):
        return {
            'deposit': self.deposit,
            'withdrawal': self.withdrawal
        }
