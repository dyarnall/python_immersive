# old_list = [1,2,3,4,2,1,1]
# new_list = [i for i in old_list if i==1]
# print(new_list)

# def cond(i):
# 	if i % 3 == 0 and i % 5 == 0:
# 		return "FizzBuzz"
# 	elif i % 3 == 0:
# 		return "Fizz"
# 	elif i % 5 == 0:
# 		return "Buzz"
# 	else:
# 		return i

# new_list = [cond(i) for i in range(1,16)]

# print(new_list)

def odd_or_even(i):
	if i % 10 == 0:
		return "{} is a Multiple of 10".format(i)
	elif i % 2 == 0:
		return "{} Is Even".format(i)
	else:
		return "{} Is Odd".format(i)

new_list = [odd_or_even(i) for i in range(1,31)]
for i in new_list:
	print(i)