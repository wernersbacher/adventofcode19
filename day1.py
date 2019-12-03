def getFuel(_weight):
	return max(int(int(_weight)/3) - 2, 0)


with open("inputs/modulemasses.txt") as mfile:

	weight = 0
	fuel_weight = 0

	for module_weight in mfile:
		# teil 1
		fuel = getFuel(module_weight)
		weight += fuel
		# teil 2

		add_weight = getFuel(fuel)
		while add_weight > 0:
			fuel_weight += add_weight
			add_weight = getFuel(add_weight)

	print("weight is {} kg".format(weight))
	print("fuel weight is {} kg, together {} kg".format(fuel_weight, weight + fuel_weight))


