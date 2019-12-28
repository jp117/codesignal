'''
https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6

Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
'''

def reverseInParentheses(inputString):
    count = countParen(inputString)
    for i in range(count):
        y = findLastParen(inputString)+1
        x = findFirstParen(inputString[:y])
        inputString = reverseInput(inputString, x, y)
    return inputString


def reverseInput(z, x, y):
    new = z[x:y][::-1]
    if countParen(new) > 0:
        x1 = findFirstParen(new)+1
        y1 = findLastParen(new)
        new = deleteParen(new, x1, y1)
    z = z[:x] + new + z[y:]
    return z


def deleteParen(z, x, y):
    z = z[y+1:x-1]
    return z


def findFirstParen(x):
    return x.rindex('(')

def findLastParen(x):
    for i in range(len(x)):
        if x[i] == ')':
            return i

def countParen(x):
    count = 0
    for i in range(len(x)):
        if x[i] == '(':
            count += 1
    return count

if __name__ == "__main__":
    print(reverseInParentheses("(bar)"))
    print(reverseInParentheses("foo(bar(baz))blim"))
    print(reverseInParentheses("(abc)d(efg)"))