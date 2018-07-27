class Customer:
	def __init__(self, name, balance=0.0):
		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeErro('Amount greater than balance')
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

def new_account():
	new_self = input("Please enter a user id: ")
	new_name = input("Please enter your name: ")
	new_balance = input("Please enter the beginning balance: ")	

	new_self = Customer(new_name, new_balance)
	return new_self.name, new_self.balance

def deposit_to_account():
	userid = input("what is your user id? ")
	dep_amount = int(input("How much to deposit? "))
	print("your old balance was $", userid.balance)
	userid.deposit(dep_amount)
	print("your new balance is $", userid.balance)
	return userid.balance



newaccount = new_account()
print("your name is", newaccount[0], "and your beginning balance is", newaccount[1])

deposit_to_account()