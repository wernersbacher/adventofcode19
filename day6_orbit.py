
def loopTupelsByName(tupelList, name):
	for row in tupelList:
		if row[0] == name:
			yield row

def loopTupelsByNameReversed(tupelList, name):
	for row in tupelList:
		if row[1] == name:
			yield row

def findChildren(tupelList, name, resultDict, depth=1):
	"""find children and calc distance"""

	for planets in loopTupelsByName(tupelList, name):
		planet, orbiter = planets
		# print(planet, orbiter, depth)
		resultDict[orbiter] = depth
		findChildren(tupelList, orbiter, resultDict, depth+1)


def findParent(tupelList, name, resultDict):

	for planets in loopTupelsByNameReversed(tupelList, name):
		planet, orbiter = planets
		# print(planet, orbiter)
		resultDict.append(planet)
		findParent(tupelList, planet, resultDict)


with open("inputs/orbit.txt") as ofile:
	space = []
	for line in ofile:
		data = line.strip().split(")")
		data_tupel = (data[0], data[1])
		space.append(data_tupel)
	print(space)

	print("DAY2:")
	print("--------------")
	youparents = []
	findParent(space, "YOU", youparents)

	santaparents = []
	findParent(space, "SAN", santaparents)

	print("--------------")
	print(youparents)
	print(santaparents)

	hops_to_santa = 0

	for dist_to_my_parent, parent in enumerate(youparents, 1):
		if parent in santaparents:
			# found parent of both!
			print(parent)
			dist_to_santas_parent = santaparents.index(parent) + 1
			#add them together, then minus 1, we don't want to hop santas orbit, he is not THAT fat
			hops_to_santa = dist_to_my_parent + dist_to_santas_parent - 1
			break # stop

	print("Distance to Santa is", hops_to_santa)

	exit()
	print("DAY1:")
	print("--------------")
	resultDict = {}

	findChildren(space, "COM", resultDict)

	print("---------------")
	print(resultDict)
	dist_sum = 0
	for planet, dist in resultDict.items():
		dist_sum += dist

	print("Distance for all stars:", dist_sum)
