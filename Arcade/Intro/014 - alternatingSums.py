'''
https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

[output] array.integer
'''

def alternatingSums(x):
    output = [0,0]
    for i in range(len(x)):
        if i%2 == 0:
            output[0] += x[i]
        else:
            output[1] += x[i]
    return output

if __name__ == "__main__":
    print(alternatingSums([50, 60, 60, 45, 70]))