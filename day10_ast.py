
import math

def calcAngle(x1, y1, x2, y2):
	myradians = math.atan2(y2-y1, x2-x1)
	return "{:.3f}".format(math.degrees(myradians))


asteroidmap = []

with open("inputs/asteroids.txt") as asfile:
	x = 0
	y = 0
	for line in asfile.readlines():
		print(line.strip())
		for location in line.strip():
			if location == "#":
				asteroidmap.append((x, y))
			x += 1
		x = 0
		y += 1

# print(asteroidmap)

asteroiddistances = {}
maxWatchable = 0

# loop over every asteroid as starter
for location in asteroidmap:
	x_here, y_here = location


	asteroiddistances[location] = []
	# print("---------")

	# loop over every other asteroid to calc the line of sight
	for other_location in asteroidmap:
		x_there, y_there = other_location

		if location == other_location:
			continue  # skip own position

		angle = calcAngle(x_here, y_here, x_there, y_there)
		if angle not in asteroiddistances[location]:
			asteroiddistances[location].append(angle)

		# print("comparing: ", location, other_location, angle)

	counted_watchable = len(asteroiddistances[location])
	if counted_watchable > maxWatchable:
		maxWatchable = counted_watchable
		bestLocation = location

print("Best Location is {} with {} watchables asteroids.".format(bestLocation, maxWatchable))

