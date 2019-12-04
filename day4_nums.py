
START = 134564
END = 585159

found = 0

for i in range(START, END+1):
	number = str(i)

	last_digit = -1

	found_double = False
	found_only_higher = True

	num_counter = {}

	for digit in number:
		intdigit = int(digit)
		# check if number before was equal or smaller
		if intdigit < last_digit:
			found_only_higher = False
			break

		# add to counter
		if intdigit in num_counter:
			num_counter[intdigit] += 1
		else:
			num_counter[intdigit] = 1

		last_digit = intdigit

	if found_only_higher:
		for number, count in num_counter.items():
			if count == 2: # make this => 2 instead of == 2 for solution of part 1
				print("Found double", i)
				found += 1
				break # break, if you dont it counts some numbers twice

print("Found {} numbers".format(found))
