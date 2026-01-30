from models.bankaccount import BankAccount

my_account = BankAccount(10000)
your_account = BankAccount(212121)

our_account = my_account + your_account
print(our_account)