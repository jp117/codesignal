'''
https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.
'''

def high(x):
    i = 0
    ans = x[0]
    while i < len(x):
        if x[i] > ans:
            ans = x[i]
            i += 1
        else: 
            i += 1
    return ans

def low(x):
    i = 0
    ans = x[0]
    while i < len(x):
        if x[i] < ans:
            ans = x[i]
            i += 1
        else:
            i += 1
    return ans

def makeArrayConsecutive2(statues):
    return high(statues) - low(statues) - len(statues) +1