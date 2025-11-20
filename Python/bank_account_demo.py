from bank_account import BankAccount

account1 = BankAccount("123", 100)
print(account1)

account2 = BankAccount("456")
print(account2)

account3 = BankAccount("789", -50)
print(account3)

account3.deposit(100)
account1.withdraw(250)

print(account1)
print(account3)