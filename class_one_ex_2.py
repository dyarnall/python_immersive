new_string = input("Please enter something: ")
letters = 0
numbers = 0

for var in new_string:
	if var.isalpha() == True:
		letters = letters + 1
	if var.isdigit() == True:
		numbers = numbers + 1
print("There are", letters, "letters and", numbers, "numbers.")