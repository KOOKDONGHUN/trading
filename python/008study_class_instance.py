class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

kim = Account('kim')
lee = Account('lee')

print(kim.num_accounts)
print(lee.num_accounts)