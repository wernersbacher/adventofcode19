WIDTH = 25
HEIGHT = 6


with open("inputs/image.txt") as imgfile:
    imgstring = imgfile.read()


PIXELS = WIDTH * HEIGHT
LAYERS = int(len(imgstring)/PIXELS)

print(PIXELS, LAYERS)
# print(imgstring)


layer_with_fewest_zeros = 0

minimalZeroes = 0
layerChecksum = 0
for i in range(LAYERS):
    start = i * PIXELS
    end = start + PIXELS
    current_layer = imgstring[start:end]
    print(current_layer)

    #the number of 1 digits multiplied by the number of 2 digits
    zeroCount = current_layer.count('0')
    if i == 0 or zeroCount < minimalZeroes:
        minimalZeroes = zeroCount
        layerChecksum = current_layer.count('1') * current_layer.count('2')
        layer_with_fewest_zeros = i

print(layerChecksum)