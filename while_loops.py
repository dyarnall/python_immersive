food = ["apple", "banana", "tomato"]

flag = True
index = 0

while flag:
	print(food[index])
	index += 1
	if food[index][0] == "t":
		flag = False
	elif index == len(food)-1:
		flag = False
	






# value = 0
# flag = True

# while flag:
# 	print(value)
# 	value += 1
# 	if value == 3:
# 		flag = False

# while value != 7:
# 	print(value, end = ' ')
# 	value += 1