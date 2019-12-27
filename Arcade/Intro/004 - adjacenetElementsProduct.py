""" 
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""

def adjacentElementsProduct(inputArray):
    i = 0
    answer = inputArray[0] * inputArray[1]
    while i < (len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > answer:
            answer = inputArray[i] * inputArray[i+1]
            i += 1
        else:
            i += 1
    return answer