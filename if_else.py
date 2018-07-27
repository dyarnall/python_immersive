# weather = input("What is the weather outside? ")
# weather = weather.lower()

# if weather == "sunny":
# 	print("Wear sunglasses!")
# elif weather == "rainy":
# 	print("Please take your umbrella.")
# elif weather == "chilly":
# 	print("Please take a sweater.")
# else:
# 	print("Have a great day!")


age = int(input("Please enter your age: "))

if age < 21 and age > 0:
	print("Sorry, you are too young to enter.")
elif age >= 21:
	print("Welcome to the club!")
else:
	print("The age you entered is invalid.")