class Credit_card:
	def __init__(self, number):
		self.number = number
		self.length = self.check_length()
		self.type = self.determine_card_type()
		self.luhn = self.luhn_check()

	def check_length(self):
		if len(self.number) == 16 or 15:
			self.length = True	
		else:
			print("card is not valid")
			self.length = False
		return self.length

	def determine_card_type(self):
		visa = ["4"]
		mast = ["51","52","53","54","55"]
		amex = ["34","37"]
		disc = ["6011"]
			
		if self.number[0] in visa:
			self.type = "visa"
		elif self.number[:2] in mast:
			self.type = "mast"
		elif self.number[:2] in amex:
			self.type = "amex"
		elif self.number[:4] in disc:
			self.type = "disc"
		else:
			self.type = "not valid"
		return self.type

	def luhn_check(self):
		reverse_number = self.number[::-1]
		luhn_modulo = 0
		if self.type != "not valid":
			for i in reverse_number:
				i = int(i)
				# print("modulo", luhn_modulo)
				if i % 2 != 0:
					double_it = i * 2
					# print("double it", double_it)
					if double_it > 9:
						double_it -= 9
					luhn_modulo += double_it
				else:
					luhn_modulo += i
		if luhn_modulo % 10 == 0:
			print ("card is valid")
			self.luhn = True
			return self.luhn
		else:
			self.luhn = False
			print("card not valid")
			return self.luhn



user = Credit_card("5515460934365316")
user.check_length()
user.determine_card_type()
user.luhn_check()
print(user.number, user.type)


