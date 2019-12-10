
import math

def calcAngle(x1, y1, x2, y2):
	myradians = math.atan2(y2-y1, x2-x1) + math.pi/2
	degrees = math.degrees(myradians)
	if degrees < 0:
		degrees += 360
	return "{:.3f}".format(degrees)

def calcDist(x1, y1, x2, y2):
	return math.hypot(x2 - x1, y2 - y1)


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
	asteroidAnglesMapped = {}

	# loop over every other asteroid to calc the line of sight
	for other_location in asteroidmap:
		x_there, y_there = other_location

		if location == other_location:
			continue  # skip own position

		angle = calcAngle(x_here, y_here, x_there, y_there)
		if angle not in asteroidAnglesMapped:
			asteroidAnglesMapped[angle] = []
		asteroidAnglesMapped[angle].append(other_location)


		if angle not in asteroiddistances[location]:
			asteroiddistances[location].append(angle)

		# print("comparing: ", location, other_location, angle)

	counted_watchable = len(asteroiddistances[location])
	if counted_watchable > maxWatchable:
		maxWatchable = counted_watchable
		homeLocation = location
		stationAngles = asteroidAnglesMapped

print("Best Location is {} with {} watchables asteroids.".format(homeLocation, maxWatchable))
# print(asteroiddistances[location])

print("PART 2 ------- ")

# get all in line of sight with coordinates
# loop over them, sorted by number, count++
# set them from # to .
# start again until count=200

print()
print(stationAngles)
SEARCH_NUMBER = 200
counter = 0
while True:
	# counter += 1

	for angle_ in sorted(stationAngles, key=float):
		print("\nRotation:", angle_)

		distMap = {}
		for location in stationAngles[angle_]:
			dist = calcDist(*homeLocation, *location)
			# print(location, dist)
			distMap[dist] = location

		distances = list(distMap.keys())
		if not distances: # skip, if empty array
			continue

		nearest_location = distMap[min(distances)]
		print(distMap)
		print("nearest location:", nearest_location)

		# removing nearest_location now
		stationAngles[angle_].remove(nearest_location)
		counter += 1
		if counter >= SEARCH_NUMBER:
			break

	if counter >= SEARCH_NUMBER:
		break

print(stationAngles)
print(counter)
print(nearest_location)