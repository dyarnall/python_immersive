temperature_celsius = float(input("What is the temperature Celsius? "))
temperature_fahrenheit = temperature_celsius * 9/5 + 32

if temperature_fahrenheit > 90:
	print(temperature_fahrenheit, "degrees fahrenheit. There is a heat warning")
elif temperature_fahrenheit < 30:
	print(temperature_fahrenheit, "degrees fahrenheit. There is a cold warning")
else:
	print(temperature_fahrenheit, "degrees fahrenheit. It is a beautiful day!")