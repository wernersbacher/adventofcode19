class Intcode:

	def __init__(self, noun=12, verb=2):

		self.memory = [1, noun, verb, 3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]

	def execute(self):
		i = 0
		while i < len(self.memory):

			opcode = self.memory[i]

			if opcode == 99:
				break

			param1 = self.memory[self.memory[i+1]]
			param2 = self.memory[self.memory[i+2]]
			dest = self.memory[i+3]

			if opcode == 1:
				self.memory[dest] = param1+param2
			elif opcode == 2:
				self.memory[dest] = param1*param2

			i += 4
			
	def dump(self):
		return self.memory

	def get(self):
		return self.memory[0]


RESULT_TO_FIND = 19690720

def findInputForOutput(out):
	for verb in range(100):
		for noun in range(100):
			computer = Intcode(verb, noun)
			computer.execute()
			if computer.get() == out:
				print("Found something")
				return verb, noun


inputs = findInputForOutput(RESULT_TO_FIND)
print(*inputs)
