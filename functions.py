# def add(a,b):
# 	total = a + b
# 	return total

# # print(add(9,1))

# def sub(a,b):
# 	total = a - b
# 	return total

# def main(a,b):
# 	x = add(a,b)
# 	s = sub(a,b)
# 	print("I am adding {} and {} and sub the results {} and {}".format(a,b,x,s))

# main(6,7)


def triangles(n):
	'''
	This makes triangles of width n
	'''


	for i in range(n):
		print(i * "*")
	for i in range(n,0,-1):
		print(i * "*")

triangles(int(input(">")))