class Intcode:

	def __init__(self, noun=12, verb=2):

		self.memory = [3,0,4,0,99]

		self.OPCODES = {
			1: {
				"operation":  (lambda x, y: x+y),
				"params": 3
			},
			2: {
				"operation": (lambda x, y: x * y),
				"params": 3
			},
			3: {
				"operation": (lambda x, y: x * y),
				"params": 1
			},
			4: {
				"operation": (lambda x, y: x * y),
				"params": 1
			}
		}

	def load(self, address):
		return self.memory[address]

	def save(self, address, value):
		self.memory[address] = value
		return True

	def execute(self):
		i = 0
		while i < len(self.memory):

			opcode = self.memory[i]

			if opcode == 99:
				break

			param_num = self.OPCODES[opcode]["params"]
			params = []

			for j in range(1, param_num+1):
				param = self.memory[i + j]
				params.append(param)


			if opcode == 1:
				result = params[0] + params[1]
				self.save(params[2], result)
			elif opcode == 2:
				result = params[0] * params[1]
				self.save(params[2], result)
			elif opcode == 3:
				userint = input("Please input a single Integer: ")
				self.save(params[0], int(userint))
			elif opcode == 4:
				print(self.load(params[0]))


			i += param_num+1

	def dump(self):
		return self.memory

	def get(self):
		return self.memory[0]


computer = Intcode()
computer.execute()