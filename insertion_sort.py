# alist = [1,9,4,7,2,2]
# sorted_portion = [alist[0]]
# unsorted_portion = alist[1:]

# for s in range(0,len(alist)-1):
# 	index_to_put_it = 0
# 	for i in range(len(sorted_portion)-1,-1,-1):
# 		if unsorted_portion[0] > sorted_portion[i]:
# 			index_to_put_it = i+1

# 			break

# 	sorted_portion.insert(index_to_put_it,unsorted_portion.pop(0))
	
#    # print("sorted_portion",sorted_portion)

# print("final sorted_portion",sorted_portion)
# 	#print("unsorted_portion",unsorted_portion)



alist = [4,9,7,101,44,2]
unsorted_list = alist[1:]
sorted_list = [alist[0]]
for s in range(0,len(alist)-1):
	index_to_put_it = 0
	for i in range(len(sorted_list)-1,-1,-1):
		if unsorted_list[0] > sorted_list[i]:
			index_to_put_it = i+1
			break
	sorted_list.insert(index_to_put_it,unsorted_list.pop(0))

print(unsorted_list,sorted_list)
