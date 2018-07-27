alist = [1,2,3,4,5]
blist = [1,2,3,4,5]

def add_one(item):
	#item = item + 1
	return item + 1

new_list = list(map(add_one,alist))
print("new list", new_list,"\nold list", alist)

def add_lists(a,b):
	# a + b
	return a + b

#new_new_list = list(map(add_lists,alist,blist))
new_new_list = list(map(lambda a,b:a+b,alist,blist))
print("new new list", new_new_list)