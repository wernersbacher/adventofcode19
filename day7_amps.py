from day5_int import Intcode
import itertools

memoryBootState = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 34, 59, 68, 89, 102, 183, 264, 345, 426, 99999, 3, 9, 102, 5,
                   9, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 1002, 9, 5, 9, 101, 5, 9, 9, 1002, 9, 3, 9, 1001,
                   9, 5, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9, 4, 9, 99, 3, 9, 102, 4, 9, 9, 101, 3, 9, 9, 102, 5, 9, 9, 101,
                   4, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 5, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
                   101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3,
                   9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4,
                   9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2,
                   9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102,
                   2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3,
                   9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4,
                   9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1,
                   9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9,
                   1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9,
                   3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9,
                   4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101,
                   1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
                   101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9,
                   99
                   ]

memoryBootStateTest=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

"""inputList = [1, 2]
resultList = []
amp1 = Intcode(memoryInput=memoryBootState, inputList=inputList, resultList=resultList)
amp1.execute()

print(resultList)"""

possibilities = list(itertools.permutations([0, 1, 2, 3, 4]))
maxSignal = 0
for permutation in possibilities:
    # print(permutation)

    pipe = 0

    for phase in permutation:
        inputList = [phase]
        resultList = []
        amp1 = Intcode(memoryInput=memoryBootState, inputList=inputList, resultList=resultList)
        amp1.execute()
        amp1.appendInput(pipe)
        # set output as input of next loop
        pipe = resultList[0]

    # print(pipe)
    if pipe > maxSignal:
        maxSignal = pipe

print("Max Signal is {} without Feedback Loop".format(maxSignal))
# exit()
print("-------")
print("PART 2:")
print("-------")


possibilities = list(itertools.permutations([5, 6, 7, 8, 9]))

maxSignal = 0
for permutation in possibilities:
    print("permutation nr.", permutation)
    pipe = 0
    ampList = []
    resultLists = []
    # set up amps
    for phase in permutation:
        new_resultList = []
        new_amp = Intcode(memoryInput=memoryBootStateTest, inputList=[phase], resultList=new_resultList)

        ampList.append(new_amp)
        resultLists.append(new_resultList)

    output_from_last_amp = 0
    pipe = 0  # inital input and input for next output
    i = 0
    num_amps = len(permutation)
    while True:
        # looping over all amps over and over again
        print("feedbacking..")
        current_amp = ampList[i]  # get current amp
        current_resultList = resultLists[i]
        current_resultList.clear()

        # append output from pre-amp
        current_amp.appendInput(pipe)

        # execute and check if halted
        if current_amp.execute() == 99:
            break # halted

        pipe = current_resultList[0]
        print(pipe)
        # cycling index
        i += 1
        if i == num_amps:
            print("start from the beginning")
            # start from beginning, save output from last amp
            i = 0
            output_from_last_amp = pipe

    if output_from_last_amp > maxSignal:
        maxSignal = output_from_last_amp

print("max output from last amp is {}".format(maxSignal))
