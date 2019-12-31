def arrayMaximalAdjacentDifference(inputArray):
    first = -16
    place = 0
    i = 0
    for i in range(len(inputArray)):
        if abs(inputArray[i]) > first:
            first = abs(inputArray[i])
            place = i
    if place > 0:
        if abs(inputArray[place]) - abs(inputArray[place-1]) > abs(inputArray[place]) - abs(inputArray[place+1]):
            return abs(inputArray[place]) - abs(inputArray[place-1])
    return abs(inputArray[place]) - abs(inputArray[place+1])

if __name__ == "__main__":
    print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))