WIDTH = 25
HEIGHT = 6


with open("inputs/image.txt") as imgfile:
    imgstring = imgfile.read()


PIXELS = WIDTH * HEIGHT
LAYERS = int(len(imgstring)/PIXELS)

print(PIXELS, LAYERS)

layerList = []

layer_with_fewest_zeros = 0

print("PART 1: ------------------------")

minimalZeroes = 0
layerChecksum = 0
for i in range(LAYERS):
    start = i * PIXELS
    end = start + PIXELS
    current_layer = imgstring[start:end]
    layerList.append(current_layer)
    # print(current_layer)

    #the number of 1 digits multiplied by the number of 2 digits
    zeroCount = current_layer.count('0')
    if i == 0 or zeroCount < minimalZeroes:
        minimalZeroes = zeroCount
        layerChecksum = current_layer.count('1') * current_layer.count('2')
        layer_with_fewest_zeros = i

print(layerChecksum)
print("PART 2: ------------------------")
print(layerList)

processed_image = []

for pixelIndex in range(PIXELS):
    processed_image.insert(pixelIndex, 2)
    print("NEXT PIXEL")
    for layerIndex in range(LAYERS):
        print("Current pixel in done picture: {}".format(processed_image[pixelIndex]))
        if processed_image[pixelIndex] != 2:
            break
            #break # jump to next pixel if proc. image is already not transparent anymore

        processed_image[pixelIndex] = int(layerList[layerIndex][pixelIndex])

print(processed_image)

print("Copy those as csv to excel")
for i in range(PIXELS):
    pixel = processed_image[i]
    print(str(pixel)+";", end='', flush=True)
    if (i+1) % WIDTH == 0:
        print()