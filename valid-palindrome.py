def isPalindrome(s):
    pureStr = [char.lower() for char in s if char.isalnum()]
    return pureStr == pureStr[::-1]