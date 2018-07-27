def store_string():
	string = input("Enter string: ")
	d = {}

	for i in string:
		d[i] = d.get(i,0) + 1
		output = list(d.items())
	for x in output:
		print(x[0], ",",x[1])

store_string()