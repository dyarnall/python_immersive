def is_a_vowel(letter):
	my_string = "aeiou"

	if letter in my_string:
		return True
	else:
		return False

def assess(word):
	if is_a_vowel(word[0]):
		pig_word = word + "yay"
		# return new_word
	else:
		for i in word:
			if is_a_vowel(i):
				log = word.index(i)
				new_word1 = word[log:]
				new_word2 = word[0:log]
				pig_word = new_word1 + new_word2 + "ay"
				# return new_word
				break
	return pig_word

def validation():
	word = input("Please enter a word: ")
	if word.isalpha() and len(word) > 1:
		print(assess(word))
	else:
		print("error")


validation()
