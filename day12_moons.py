class Dimension:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def getAbs(self):
		return abs(self.x)+abs(self.y)+abs(self.z)

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
