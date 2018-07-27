num = int(input("Enter the first number number: "))
size_list = []
flag = True

while flag:
	num2 = int(input("Enter the next number: "))
	if num2 == 0:
		flag = False
	elif num2 == num:
		size = "Same"
	elif num2 > num:
		size = "Up"
	else:
		size = "Down"
	size_list.append(size)
	num = num2
for i in size_list:
	print(i, end = " ")
