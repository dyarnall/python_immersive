class Credit_card:
	def __init__(self, number):
		self.number = self.luhn_check()
		self.length = self.check_length()
		self.type = None

	def check_length(self, number):
		if self.number != 16 or 15:
			raise print("card is not valid")
		else:
			self.length = True
		return self.length

	def determine_card_type(self, number):
		prefix2 = [51,52,53,54,55,34,37]

		if cc_input[0] == 4:
			self.type = True
		else:
			if cc_input[0:2] in prefix2:
				self.type = True
			elif self.number[0:4] == 6011:
				self.type = True
			else:
				raise print("card not valid")
		return self.type = True

	def luhn_check(self, number)
		luhn_modulo = 0
		if self.type:
			for i in cc_input[-1::-2]:
				if cc_input[i] % == 0:
					double_it = cc_input[1] *2
					if len(double_it) > 10:
						double_it -= 9
				else:
					luhn_modulo += cc_input[i]
			for s in range(len(luhn_list)):
				if luhn_modulo % 10 == 0:
					return cc_input
				else:
					raise print("card not valid")






