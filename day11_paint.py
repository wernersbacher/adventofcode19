from day5_int import Intcode

memoryBootState = [3,8,1005,8,330,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,28,1,1103,17,10,1006,0,99,1006,0,91,1,102,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,64,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,86,2,4,0,10,1006,0,62,2,1106,13,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,120,1,1109,1,10,1,105,5,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,149,1,108,7,10,1006,0,40,1,6,0,10,2,8,9,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,187,1,1105,10,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,213,1006,0,65,1006,0,89,1,1003,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,244,2,1106,14,10,1006,0,13,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,273,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,295,1,104,4,10,2,108,20,10,1006,0,94,1006,0,9,101,1,9,9,1007,9,998,10,1005,10,15,99,109,652,104,0,104,1,21102,937268450196,1,1,21102,1,347,0,1106,0,451,21101,387512636308,0,1,21102,358,1,0,1105,1,451,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,97751428099,1,21102,1,405,0,1105,1,451,21102,1,179355806811,1,21101,416,0,0,1106,0,451,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,868389643008,1,21102,439,1,0,1105,1,451,21102,1,709475853160,1,21102,450,1,0,1105,1,451,99,109,2,22102,1,-1,1,21101,0,40,2,21101,482,0,3,21102,1,472,0,1105,1,515,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,477,478,493,4,0,1001,477,1,477,108,4,477,10,1006,10,509,1101,0,0,477,109,-2,2105,1,0,0,109,4,2101,0,-1,514,1207,-3,0,10,1006,10,532,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21101,1,0,3,21101,0,551,0,1105,1,556,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,579,2207,-4,-2,10,1006,10,579,22102,1,-4,-4,1105,1,647,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,598,0,1106,0,556,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,617,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,639,22102,1,-1,1,21102,1,639,0,105,1,514,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0
]

BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1

def calcRobotMovement(x, y, direction, rotating):
	if rotating == LEFT:
		direction = (direction-1) % 4
	if rotating == RIGHT:
		direction = (direction+1) % 4

	if direction == 0:
		y -= 1
	elif direction == 1:
		x += 1
	elif direction == 2:
		y += 1
	elif direction == 3:
		x -= 1

	return x, y, direction



outputHolder = []
robot = Intcode(memoryInput=memoryBootState, resultList=outputHolder, inputList=[])

coloredmap = {}
current_color = BLACK
current_direction = 0
x = 0
y = 0

# change here the starting color to get to part 1 == black or part 2 == white

coloredmap[(x, y)] = WHITE

while True:
	#load the color at the current coodinate
	coordinates = (x, y)
	print("\nstarting at coordinates {}, direction: {}".format(coordinates, current_direction))
	if coordinates in coloredmap:
		current_color = coloredmap[coordinates]
		print("found color")
	else:
		current_color = BLACK
		print("use default color")

	# execute robot and check if finished
	return_code = robot.appendInput(current_color)
	if return_code == 99:
		print("Robot has finished")
		break

	# get color and rotating output
	new_color, rotating = outputHolder
	outputHolder.clear()
	print("new color is {} and turn to {}".format(new_color, rotating))

	# save the new color
	coloredmap[coordinates] = new_color

	# move the ship
	x, y, current_direction = calcRobotMovement(x, y, current_direction, rotating)

print(coloredmap)
print(len(coloredmap))

for i in range(8):

	for j in range(50):
		coords = j, i
		toPrint = " "
		if coords in coloredmap and coloredmap[coords] == WHITE:
			toPrint = "█"
		print(toPrint, end="", flush=True)

	print("; ")
