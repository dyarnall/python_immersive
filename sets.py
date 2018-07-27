# a = [1,2,3,3,2,1,5,6,5,5,5]
# b = [1,4,6,6,7,3,9,0,0,0]
# new_set_a = set(a)
# new_set_b = set(b)
# print(new_set_a, new_set_b)

# intersect = new_set_a.intersection(new_set_b)
# print(intersect)

new_set = set()

def add_to_set(word):
	new_set.add(word)
	if word == "quit":
		flag = False
	else: 
		flag = True
	return flag

def main():
	flag = True

	while flag:
		word = input("Add any word: ")
		flag = add_to_set(word)

main()
print("These are all of the unique words you entered: ", new_set)


