letter = input("Please enter a letter: ")
letter = letter.lower()
vowel = ["a", "e", "i", "o", "u"]

if letter in vowel:
	print(letter, "is a vowel.")
elif letter == "y":
	print(letter, "is sometimes a vowel.")
else:
	print(letter, "is a consonant.")