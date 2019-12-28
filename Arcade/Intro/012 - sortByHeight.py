'''
https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

[output] array.integer

Sorted array a with all the trees untouched.
'''

def sortByHeight(a):
    x = checkPeople(a)
    x.sort()
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = x[0]
            x.remove(x[0])
    return a

def checkPeople(a):
    output = []
    for i in range(len(a)):
        if a[i] != -1:
            output.append(a[i])
    return output

if __name__ == "__main__":
    print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))