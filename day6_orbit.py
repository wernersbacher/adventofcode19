
def loopTupelsByName(tupelList, name):
	for row in tupelList:
		if row[0] == name:
			yield row


def findChildren(tupelList, name, resultDict, depth=1):
	"""find children and calc distance"""

	for planets in loopTupelsByName(tupelList, name):
		planet, orbiter = planets
		print(planet, orbiter, depth)
		resultDict[orbiter] = depth
		findChildren(tupelList, orbiter, resultDict, depth+1)


with open("inputs/orbit.txt") as ofile:
	space = []
	for line in ofile:
		data = line.strip().split(")")
		data_tupel = (data[0], data[1])
		space.append(data_tupel)
	print(space)
	print("--------------")
	resultDict = {}

	findChildren(space, "COM", resultDict)

	print("---------------")
	print(resultDict)
	dist_sum = 0
	for planet, dist in resultDict.items():
		dist_sum += dist

	print("Distance for all stars:", dist_sum)
