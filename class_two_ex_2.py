def capitalize_first_letter(user_string):
	user_string = user_string.capitalize()
	return user_string

def capitalize_new_sentence(user_string):
	special_char = ".?!"
	str_for_user = ""
	for index in range(0, len(user_string)):
		if user_string[index] in special_char:
			user_string = user_string[0:index+2] + user_string[index+2:].capitalize()
			str_for_user += user_string[index]
		else:
			str_for_user += user_string[index]
	return str_for_user

def capitalize_i(str_for_user):
	low_i = " i "
	cap_i = " I "

	if low_i in str_for_user:
			new_string = str_for_user.replace(low_i, cap_i)
			print(new_string)

def main():
	user_string = input("Please enter something: ")
	capitalized_string = capitalize_first_letter(user_string)
	capitalized_all = capitalize_new_sentence(capitalized_string)
	capitalize_i(capitalized_all)


main()


