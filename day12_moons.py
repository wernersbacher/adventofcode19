import time
import numpy as np


def lcm(x, y):
	# choose the greater number
	if x > y:
		greater = x
	else:
		greater = y
	while True:
		if (greater % x == 0) and (greater % y == 0):
			lcm = greater
			break
		greater += 1
	return lcm


class Dimension:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def getAbs(self):
		return abs(self.x) + abs(self.y) + abs(self.z)


class Moon:

	def __init__(self, posX, posY, posZ):

		self.position = Dimension(posX, posY, posZ)
		self.velocity = Dimension()

	def calcPull(self, pos, other_pos):
		if other_pos > pos:
			return 1
		elif pos > other_pos:
			return -1
		return 0

	def calcVelocityX(self):
		self.velocity.x += self.calcPull(self.position.x, other_moon.position.x)

	def calcVelocityY(self):
		self.velocity.y += self.calcPull(self.position.y, other_moon.position.y)

	def calcVelocityZ(self):
		self.velocity.z += self.calcPull(self.position.z, other_moon.position.z)

	# part 1 methods

	def calcVelocity(self, other_moon):
		# update velocity
		self.velocity.x += self.calcPull(self.position.x, other_moon.position.x)
		self.velocity.y += self.calcPull(self.position.y, other_moon.position.y)
		self.velocity.z += self.calcPull(self.position.z, other_moon.position.z)

	def applyVelocity(self):
		self.position.x += self.velocity.x
		self.position.y += self.velocity.y
		self.position.z += self.velocity.z

	def getEnergy(self):
		return self.velocity.getAbs() * self.position.getAbs()


moons = []

# building moon objects from text input
with open("inputs/moons.txt") as moonfile:
	for line in moonfile.readlines():
		coords = line.strip().replace("<", "").replace(">", "").replace(" ", "").split(",")
		coord_clean = []
		for part in coords:
			coord_clean.append(int(part.split("=")[1]))

		new_moon = Moon(*coord_clean)
		moons.append(new_moon)

# find x period for repeating pattern
xSteps = 0
starting_state = []
while True:
	universum_state = []
	# calc all velocitys first
	for moon in moons:
		for other_moon in moons:
			moon.velocity.x += moon.calcPull(moon.position.x, other_moon.position.x)
	# calc new position and set the state to the universum_state
	for moon in moons:
		moon.position.x += moon.velocity.x
		universum_state.append((moon.position.x, moon.velocity.x))

	if universum_state == starting_state:
		print("Found step")
		break
	elif xSteps == 0:
		starting_state = universum_state

	# print("Step {}, current universum_state: ".format(xSteps), universum_state, starting_state)
	# time.sleep(1)
	xSteps += 1


print("PART 1 ----------------------")
"""
	DISCLAIMER: COPY AND PASTE Code, should be refactored for "real-world"-use.
"""

# find y period for repeating pattern
ySteps = 0
starting_state = []
while True:
	universum_state = []
	# calc all velocitys first
	for moon in moons:
		for other_moon in moons:
			moon.velocity.y += moon.calcPull(moon.position.y, other_moon.position.y)
	# calc new position and set the state to the universum_state
	for moon in moons:
		moon.position.y += moon.velocity.y
		universum_state.append((moon.position.y, moon.velocity.y))

	if universum_state == starting_state:
		print("Found step")
		break
	elif ySteps == 0:
		starting_state = universum_state

	# print("Step {}, current universum_state: ".format(ySteps), universum_state)
	ySteps += 1

# find z period for repeating pattern
zSteps = 0
starting_state = []
while True:
	universum_state = []
	# calc all velocitys first
	for moon in moons:
		for other_moon in moons:
			moon.velocity.z += moon.calcPull(moon.position.z, other_moon.position.z)
	# calc new position and set the state to the universum_state
	for moon in moons:
		moon.position.z += moon.velocity.z
		universum_state.append((moon.position.z, moon.velocity.z))

	if universum_state == starting_state:
		print("Found step")
		break
	elif zSteps == 0:
		starting_state = universum_state

	# print("Step {}, current universum_state: ".format(zSteps), universum_state)
	zSteps += 1

print("Found alle steps, calculating lcm")
print(xSteps, ySteps, zSteps)
#print(lcm(lcm(xSteps, ySteps), zSteps))
lcm_val = np.lcm.reduce([xSteps, ySteps, zSteps])
print(lcm_val)

exit()
print("PART 1 ----------------------")

for i in range(1000):
	for moon in moons:
		for other_moon in moons:
			moon.calcVelocity(other_moon)

	for moon in moons:
		moon.applyVelocity()

system_energy = 0
for moon in moons:
	print("Moons i: --------------")
	print(moon.position.x, moon.position.y, moon.position.z)
	print(moon.velocity.x, moon.velocity.y, moon.velocity.z)
	system_energy += moon.getEnergy()

print("System Energy is {}".format(system_energy))
