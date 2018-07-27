cost_of_meal = float(input("How much was your meal? "))
# print("Before", type(cost_of_meal))
# cost_of_meal = float(cost_of_meal)
# print("After", type(cost_of_meal))

tax_rate = .08
tip = .18

tax_total = cost_of_meal * tax_rate
tip_total = cost_of_meal * tip

meal_total = cost_of_meal + tax_total + tip_total

print(meal_total)