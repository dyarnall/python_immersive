word_list = []
flag = True

while flag:
	user_word = input("Please enter a word: ")
	if user_word == "quit":
		flag = False
	elif user_word not in word_list:	
		word_list.append(user_word)
 for i in word_list:
			print(i)


	