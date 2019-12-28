'''
https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
'''

def palindromeRearranging(x):
    letters = {}
    for i in x:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    if len(x) % 2 == 0:
        for key, value in letters.items():
            if value % 2 != 0:
                return False
        return True
    if len(x) % 2 == 1:
        count = 0
        while count < 1:
            for key, value in letters.items():
                if value % 2 != 0:
                    count += 1
        if count > 1:
            return False
        if count <= 1:
            return True

if __name__ == "__main__":
    print(palindromeRearranging('aabb'))
    print(palindromeRearranging('abbcabb'))
        
