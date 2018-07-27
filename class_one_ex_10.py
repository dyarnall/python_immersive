user_word = input("Please enter a word to encrypt: ")
shift = int(input("Please enter a shift amount: "))
shift = shift % 26
encrypt = []

for i in user_word:
	if i.isalpha() == True:
		i = ord(i) + shift
		encrypt.append(chr(i))
	else:
		encrypt.append(i)
for i in encrypt:
	print(i, end = '')
