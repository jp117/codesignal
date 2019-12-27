'''
https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
'''

def checkLength(inputArray):
    i = 0
    length = 0
    for i in range(len(inputArray)):
        x = len(inputArray[i])
        if x > length:
            length = x
    return length

def allLongestStrings(inputArray):
    i = 0
    length = checkLength(inputArray)
    output = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) == length:
            output.append(inputArray[i])
    return output
