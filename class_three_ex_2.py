def main():
	value = input("enter a word: ")
	reverse = reverse_look_up(value)

def reverse_look_up(value):
	keys = list(d.items())
	for i in keys:
		if value == i[1]:
			print(i[0])

def unpacking(tup):
	return tup[0]


d = {}

d["le"] = "the"
d["chat"] = "cat"
d["livre"] = "book"
d["pomme"] = "apple"
d["wrong"] = "the"
d["again"] = "the"

main()
