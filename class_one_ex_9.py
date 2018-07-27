user_word = input("Please enter a word: ")
user_word = user_word.lower()
# word_list1 = []
# word_list2 = []

# for char in user_word:
# 	word_list1.append(char)
# for char in user_word[-1::-1]:
# 	word_list2.append(char)
# if word_list1 == word_list2:
# 	print(user_word, "is a palindrome.")
# else:
# 	print(user_word, "is not a palindrome.")

backwards_word = user_word[-1::-1]
if user_word == backwards_word:
	print(user_word, "is a palindrome.")
else:
	print(user_word, "is not a palindrome.")

