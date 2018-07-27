a_list = [1,2,55,1,9,4,56,2,1,8]

# print("There are", a_list.count(1), "ones in the list.")

total_ones = 0

for var in a_list:
	if var == 1:
		total_ones = total_ones + 1
print("There are", total_ones, "ones in the list.")
	
