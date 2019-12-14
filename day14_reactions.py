import math, time

def findOres(reactionstree, resultList, wastedList, name, wanted_amount):
    # print()
    # print("name: ", name)
    reaction = reactiontree[name]
    smallest_amount = reaction["num"]
    # init wasted list, if first time seeing this child
    if name not in wastedList:
        wastedList[name] = 0

    while wastedList[name] >= 1:
        wastedList[name] -= 1
        wanted_amount -= 1

    reaction_repeats = math.ceil(wanted_amount/smallest_amount)
    # print("reaction_repeats ", reaction_repeats)
    reaction_result_amount = smallest_amount * reaction_repeats

    if wanted_amount == 0:
        # print("Dont run reaction again pls")
        return

    wasted_material = reaction_result_amount - wanted_amount
    wastedList[name] += wasted_material
    # print("wasted_material", wasted_material)


    for child, child_needed in reaction["children"].items():

        # print("--- parent: ",name, "child: ", child, " child_needed: ", child_needed)

        # calc how much children are needed
        used_children_num = child_needed * reaction_repeats

        if child == "ORE":
            resultList["ORE"] += used_children_num
        else: # call findores again
            findOres(reactiontree, resultList, wastedList, child, used_children_num)
        # print("child ", child, " done")

reactiontree = {}
# building reaction tree
with open("inputs/reactions.txt") as rfile:

    for line in rfile.readlines():
        sides = line.strip().split("=>")
        children = sides[0].split(", ")

        num_target, target = sides[1].strip().split(" ")

        childrenTree = {}
        for child in children:
            num_comp, component = child.strip().split(" ")
            childrenTree[component] = int(num_comp)

        reactiontree[target] = {"num": int(num_target), "children": childrenTree}

print(reactiontree)

print("Part 1: -------------")

results = {"ORE":0}
wasted = {"ORE":0}
findOres(reactiontree, results, wasted, "FUEL", 1)

print("---------------")
print(results)
print(wasted)

print("Part 2: faster approach: -------------")

successMulti = 1 # +1 now matter what, so we start at *2

fuelToBeProduced = 1
fuelProduced = 0

oresLeft = 1000000000000

wasted = {"ORE":0}
wastedPastState = None
while fuelToBeProduced > 0:
    time.sleep(.1)
    print(fuelToBeProduced, oresLeft)
    results = {"ORE": 0}
    wastedPastState = wasted # save, if we have to restore state
    findOres(reactiontree, results, wasted, "FUEL", fuelToBeProduced)

    used_ores = results["ORE"]
    if used_ores > oresLeft:
        # requestes fuel too big; skip
        wasted = wastedPastState
        fuelToBeProduced = int(fuelToBeProduced/(2.3)) # reset to state before that loop
        successMulti /= 2
        print("skipped")
        continue

    oresLeft -= used_ores
    fuelProduced += fuelToBeProduced
    # fuelToBeProduced = int(fuelToBeProduced * (1 + successMulti))
    fuelToBeProduced *= 2

print("We produced {} litre of fuel".format(fuelProduced))