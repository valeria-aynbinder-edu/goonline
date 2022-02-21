class BanksManager:

    def __init__(self):
        self.banks = {}

    def create_bank(self, bank_name):
        bank = Bank(bank_name)
        self.banks[bank_name] = bank

    def transfer(self, from_bank, from_account, to_bank, to_account, amount):
        from_bank_obj = self.banks[from_bank]
        from_account_obj = from_bank_obj.accounts[from_account]
        from_account_obj.withdraw(amount)


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name #discount
        self.accounts = {}

    def open_account(self, customer_name):
        account = Account(customer_name, 123, self.bank_name)
        self.accounts[123] = account




class Account:
    def __init__(self, customer_name, account_num, bank_name):
        self.customer_name = customer_name
        self.account_num = account_num
        self.bank_name = bank_name

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount, another_account):
        self.withdraw(amount)
        another_account.deposit(amount)
