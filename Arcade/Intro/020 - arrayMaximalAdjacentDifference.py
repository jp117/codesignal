def arrayMaximalAdjacentDifference(inputArray):
    i = 0;
    difference = -15
    for i in range(len(inputArray)-1):
        if i == 0:
            if abs(inputArray[i] - inputArray[i+1]) > difference:
                difference = abs(inputArray[i] - inputArray[i+1])
        elif (i < (len(inputArray)-1)):
            if abs(inputArray[i] - inputArray[i-1]) > difference:
                difference = abs(inputArray[i] - inputArray[i-1])
            if abs(inputArray[i] - inputArray[i+1]) > difference:
                difference = abs(inputArray[i] - inputArray[i+1])
        else:
            if abs(inputArray[i] - inputArray[i-1]) > difference:
                difference = abs(inputArray[i] - inputArray[i-1])
    return difference


if __name__ == "__main__":
    print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))
    print(arrayMaximalAdjacentDifference([10, 11, 13]))
    print(arrayMaximalAdjacentDifference([-1, 1, -3, -4]))