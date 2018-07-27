alist = [4,9,7,101,44,2,11,43,65,23,2,4,99,34,21]
length = len(alist)

def swap_numbers(alist):
	
	for a in range(length-1):
		for a in range(length-1):
			b = a + 1
			if alist[a] > alist[b]:
				alist[a], alist[b] = alist[b],alist[a]
	return alist	

swap_numbers(alist)
print(alist)
