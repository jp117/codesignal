"""Given the string, check if it is a palindrome."""

def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False