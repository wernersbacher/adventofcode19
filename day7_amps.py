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

memoryBootStateTest=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

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
        new_resultList = []  # this is the place where the output from the program gets written to, yes its hacky
        new_amp = Intcode(memoryInput=memoryBootState, inputList=[phase], resultList=new_resultList)

        ampList.append(new_amp)
        resultLists.append(new_resultList)

    output_from_last_amp = 0
    pipe = 0  # initial input and input for next output
    i = 0
    num_amps = len(permutation)
    while True:
        # looping over all amps over and over again
        old_pipe = pipe
        current_amp = ampList[i]  # get current amp
        current_resultList = resultLists[i]
        current_resultList.clear()

        # append output from pre-amp
        current_amp.appendInput(pipe)

        pipe = current_resultList[0]
        # execute and check if halted
        execution_code = current_amp.execute()
        if execution_code == 99 and i == num_amps-1:
            print("halted from exit code 99")
            print("halted pipe: {}".format(pipe))

            output_from_last_amp = pipe
            break # halted

        print("Cycle number {} with input: {} and output: {}".format(i, old_pipe, pipe))
        # cycling index
        i = (i+1) % num_amps

    print("Last amp value in this perm: {}".format(output_from_last_amp))

    if output_from_last_amp > maxSignal:
        maxSignal = output_from_last_amp
        maxPerm = permutation

print("max output from last amp is {} when using perm {}".format(maxSignal, maxPerm))
