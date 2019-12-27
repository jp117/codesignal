'''
https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
'''


def commonCharacterCount(s1, s2):
    count = 0
    i = 0
    
    for i in range(len(s1)):
        if s1[i] in s2:
            s2 = s2.replace(s1[i], '', 1)
            count += 1
    return count