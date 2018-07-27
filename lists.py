# name = "David"

# time = int(input("What time is it? "))
# friends = ["Mark", "Emily", "John"]
# friends = "David"

# for name in friends:
	# if time < 7:
	# 	print("Hello,",name.upper(), "Party starts at 7.")
	# elif time == 7:
	# 	print("Hello,", name, "you are right on time.")
	# else:
	# 	print(name, "You are late.")


shopping_list = ["bananas", "Oranges", "Apples", "Coconut Water"]
new_item = input("What else should I get? ")
shopping_list.append(new_item)

for name in shopping_list:
	if name == "bananas":
		print("Hmm, I like", name)
	else:
		print(name, "is also fine.")