
def dictFromList(lis):
	dic = {}
	for i, value in enumerate(lis):
		dic[i] = value
	return dic


class Intcode:

	def __init__(self, inputList=None, memoryInput=None, resultList=None, noun=12, verb=2):

		if memoryInput is not None:
			self.memoryBootState = memoryInput[:]
		else:
			self.memoryBootState = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,45,16,225,2,65,191,224,1001,224,-3172,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,90,55,225,101,77,143,224,101,-127,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1102,52,6,225,1101,65,90,225,1102,75,58,225,1102,53,17,224,1001,224,-901,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1002,69,79,224,1001,224,-5135,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,102,48,40,224,1001,224,-2640,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,50,22,225,1001,218,29,224,101,-119,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1101,48,19,224,1001,224,-67,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1101,61,77,225,1,13,74,224,1001,224,-103,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,28,90,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,479,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,539,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,569,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226
]

		self.memory = dictFromList(self.memoryBootState)

		self.useInputList = False
		if inputList is not None:
			self.useInputList = True
			self.inputList = inputList[:]

		self.useResultList = False
		if resultList is not None:
			self.useResultList = True
			self.resultList = resultList
		# states
		self.ip = 0
		self.relativeBase = 0
		self.paused = False
		self.OPCODES = {
			1: {
				"params": 3
			},
			2: {
				"params": 3
			},
			3: {
				"params": 1
			},
			4: {
				"params": 1
			},
			5: {
				"params": 2
			},
			6: {
				"params": 2
			},
			7: {
				"params": 3
			},
			8: {
				"params": 3
			},
			9: {
				"params": 1
			}
		}

	def getNextInput(self):
		if self.useInputList:
			# print(self.inputList)
			if self.inputList:
				userint = self.inputList.pop(0)
			else:
				# wait for input
				self.waitForInput()
				return "halt"
		else:
			userint = input("Please input a single Integer: ")
		return userint

	def output(self, value):
		if self.useResultList:
			self.resultList.append(value)
		else:
			print(value)

	def waitForInput(self):
		# print("Wait for input ...")
		self.paused = True

	def appendInput(self, value):
		# print("Appending input")
		if not self.useInputList:
			return False
		self.inputList.append(value)

		return self.execute()

	def load(self, address):
		if address in self.memory:
			return self.memory[address]
		else:
			return 0

	def load_mode(self, params):
		param, mode = params["param"], params["mode"]
		if int(mode) == 1: # return literal value
			return param
		elif int(mode) == 2: # return memory(address+base)
			return self.load(param+self.relativeBase)

		return self.load(param) # return memory(address)

	def save(self, address, value):
		self.memory[address] = value
		return True

	def save_mode(self, params, value):
		param, mode = params["param"], params["mode"]
		if int(mode) == 2:  # save to memory(address+base)
			# print("save at location nr {}, {}".format(param, self.relativeBase))
			return self.save(param + self.relativeBase, value)
		return self.save(param, value)  # save to memory(address)

	def execute(self):
		self.paused = False
		while not self.paused:
			# print("current ip: {}".format(self.ip))
			opcode = self.load(self.ip)
			opcode_string = f'{opcode:05d}' # padded with zeros
			opcode_command = int(opcode_string[-2:])
			opcode_modes = opcode_string[:-2]

			increase_ip_auto = True

			if opcode_command == 99:
				return 99

			# get number of params
			param_num = self.OPCODES[opcode_command]["params"]
			params = []

			# read params and modes
			for j in range(1, param_num+1):
				param = self.load(self.ip + j)
				mode = opcode_modes[-j]
				params.append({"param": param, "mode": mode})

			# add x + y
			if opcode_command == 1:
				value1 = self.load_mode(params[0])
				value2 = self.load_mode(params[1])
				result = value1 + value2
				self.save_mode(params[2], result)
			# mul x * y
			elif opcode_command == 2:
				value1 = self.load_mode(params[0])
				value2 = self.load_mode(params[1])
				result = value1 * value2
				self.save_mode(params[2], result)

			#input int
			elif opcode_command == 3:
				userint = self.getNextInput()
				if not self.paused:
					self.save_mode(params[0], int(userint))

			#output int
			elif opcode_command == 4:
				self.output(self.load_mode(params[0]))

			# jump if true
			elif opcode_command == 5:
				test_value = self.load_mode(params[0])
				if test_value != 0:
					jump_target = self.load_mode(params[1])
					self.ip = jump_target
					increase_ip_auto = False

			# jump if false
			elif opcode_command == 6:
				test_value = self.load_mode(params[0])
				if test_value == 0:
					jump_target = self.load_mode(params[1])
					self.ip = jump_target
					increase_ip_auto = False

			# less than
			elif opcode_command == 7:
				cmp1 = self.load_mode(params[0])
				cmp2 = self.load_mode(params[1])
				result = 0
				if cmp1 < cmp2:
					result = 1

				self.save_mode(params[2], result)

			# equal
			elif opcode_command == 8:
				cmp1 = self.load_mode(params[0])
				cmp2 = self.load_mode(params[1])
				result = 0
				if cmp1 == cmp2:
					result = 1

				self.save_mode(params[2], result)

			# set relative
			elif opcode_command == 9:
				relative_address_change = self.load_mode(params[0])
				self.relativeBase += relative_address_change


			if increase_ip_auto and not self.paused:
				self.ip += param_num+1

		return 0

	def dump(self):
		return self.memory

	def get(self):
		return self.memory[0]


if __name__ == "__main__":

	computer = Intcode(inputList=[5])
	computer.execute()

	# print(computer.dump())
