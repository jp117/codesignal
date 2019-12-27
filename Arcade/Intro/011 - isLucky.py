'''
https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
'''

def isLucky(n):
    length = len(str(n))
    x = length / 2
    one = 0
    two = 0
    for i in range(length):
        while i <= x-1:
            one += int(str(n)[i])  
            break
        while i >= x:
            two += int(str(n)[i])
            break
        i += 1
    if one == two:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isLucky(1230))
    