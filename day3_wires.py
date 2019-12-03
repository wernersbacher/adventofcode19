
def calcDist(x, y):
	return abs(x)+abs(y)

def calcDistBetweenStartEnd(start, end):
	return abs(start["x"]-end["x"]) + abs(start["y"]-end["y"])

def inInterval(left, middle, right):
	if left <= middle <= right or right <= middle <= left:
		return True
	return False

def check_overlap(start1, end1, start2, end2, allowSwitch=True):

	# switch the direction of the lines for the algorithm
	if start2["x"] == end2["x"] and allowSwitch:
		start1, start2 = start2, start1
		end1, end2 = end2, end1

	# print(inInterval(start2["x"], start1["x"], end2["x"]))
	if not inInterval(start2["x"], start1["x"], end2["x"]):
		# print("not in interval1")
		return False

	if not inInterval(start1["y"], start2["y"], end1["y"]):
		# print("not in interval2")
		return False

	# at this point, we can be sure that the lines interact with each other

	crosspoint = (start1["x"], start2["y"])

	return crosspoint

def check_point_on_line(start, end, point):
	if not inInterval(start["x"], point["x"], end["x"]):
		return False
	if not inInterval(start["y"], point["y"], end["y"]):
		return False

	return True


res1 = check_overlap({"x": 1, "y": 0}, {"x": 1, "y": 4}, {"x": 0, "y": 2}, {"x": 3, "y": 2})
res2 = check_overlap({"x": 1, "y": 0}, {"x": 1, "y": 1}, {"x": 0, "y": 2}, {"x": 3, "y": 2})
res3 = check_point_on_line({'x': 6, 'y': 3}, {'x': 2, 'y': 3}, {'x': 4, 'y': 3})

print(res1, res2, res3)

print(calcDistBetweenStartEnd({"x": 1, "y": 0}, {'x': 1, 'y': 3}))

# exit()

with open("inputs/wire_directions_small.txt") as wirefile:
	# loop through lines =^ wires
	all_wires = []
	crosspoints = []
	for i, line in enumerate(wirefile):
		directions = line.split(",")

		this_wire_lines = []
		current_position = {"x": 0, "y": 0}
		this_wire_lines.append(current_position.copy())

		# loop through directions for the wire
		for direction in directions:
			command = direction[0]
			distance = int(direction[1:].strip())

			# change positions
			if command == "L":
				current_position["x"] -= distance
			elif command == "R":
				current_position["x"] += distance
			elif command == "U":
				current_position["y"] += distance
			elif command == "D":
				current_position["y"] -= distance

			# append current pos to the line info
			this_wire_lines.append(current_position.copy())

		# directions are done, adding the set of points/lines to the global dict
		all_wires.append(this_wire_lines)

	# at this point we got all points where the line is at
	# print(all_wires)

	# going over all wires to check if there are overlappings with other ones
	for i, wire in enumerate(all_wires):
		print("Wire:", wire)

		# loop over segments/lines of the i-wire
		for j, segment in enumerate(wire):
			if j == len(wire) - 1: # stop if end of wire reached
				break
			start = wire[j]
			end = wire[j+1]

			# loops over all wires, but only those who havn't been checked yet
			for other_wire in all_wires[i + 1:]:
				for k, other_segment in enumerate(other_wire):
					if k == len(other_wire) - 1:  # stop if end of other wire reached
						break
					other_start = other_wire[k]
					other_end = other_wire[k + 1]

					# now we have the coordinates to compare, start comparing
					result = check_overlap(start, end, other_start, other_end)
					print(start, end, other_start, other_end)
					if result:
						crosspoints.append(result)

	# PART 1

	# going trhou crosspoints
	min_dist = -1
	nearest_point = None
	for point in crosspoints:

		print("We got a match at x = {}, y = {}.".format(*point))
		dist = calcDist(*point)
		print(dist)

		if min_dist < 0 < dist or 0 < dist < min_dist:
			min_dist = dist
			nearest_point = point

	print("Nearest distance is {}".format(min_dist), nearest_point)

	# PART 2

	all_wire_distances = []
	# going through the lines (again) to calc the dist
	for i, wire in enumerate(all_wires):

		wire_cross_distances = {}
		distance_made = 0 # start at zero

		# loop over segments/lines of the i-wire
		for j, segment in enumerate(wire):
			if j == len(wire) - 1: # stop if end of wire reached (no next point)
				break
			start = wire[j]
			end = wire[j+1]

			print("----")
			print(start, end)
			for cross in crosspoints:
				point = {"x": cross[0], "y": cross[1]}
				print(i, j, point)
				if check_point_on_line(start, end, point):
					distance_from_start = calcDistBetweenStartEnd(start, point)
					print("Found cross on line!", distance_made+distance_from_start)
					# add dist to point to distance
					wire_cross_distances[cross] = distance_made+distance_from_start

			distance_made += calcDistBetweenStartEnd(start, end)

		all_wire_distances.append(wire_cross_distances)

	print(all_wire_distances)

	smallest_dist = -1
	# hardcoded for two lines
	for point, dist in all_wire_distances[0].items():
		if point not in all_wire_distances[1]:
			continue # skip if the point is not in other one

		dist_accumlated = dist + all_wire_distances[1][point]
		if smallest_dist < 0 < dist_accumlated or dist_accumlated < smallest_dist:
			smallest_dist = dist_accumlated

	print("smallest dist to a intersection is {}".format(smallest_dist))

