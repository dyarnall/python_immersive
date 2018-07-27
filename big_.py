number = int(input("enter a number one to seven "))
alist = [1,2,3,5,6,7,8]
end = len(alist)-1
start = 0
flag = False

while not flag and start != end:
	middle_index = (start + end) // 2

	if number == alist[middle_index]:
		print("your number is in the list")
		flag = True
	else:
		if number < alist[middle_index]:
			end = middle_index
		else:
			start = middle_index	




