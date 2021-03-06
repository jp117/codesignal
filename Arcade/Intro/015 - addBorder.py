'''
https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.
'''

def addBorder(x):
    length = len(x[0])
    new = ''
    for i in range(length):
        new += '*'
    x.insert(0, new)
    x.append(new)
    length = len(x)
    for i in range(length):
        x[i] = '*' + x[i] + '*'
    return x

if __name__ == "__main__":
    print(addBorder(['abc', 'ded']))