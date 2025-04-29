def isPalindrome(s):
    pureStr = [char.lower() for char in s if char.isalnum()]
    # Solution 1 -- the easiest one but costy
    # return pureStr == pureStr[::-1]
    
    # Solutin 2 -- Two pointer (optimal)
    # left = 0
    # right = len(s) - 1
    
    # while left < right:
    #     if pureStr[left] != pureStr[right]:
    #         return False
    #     left += 1
    #     right -= 1
    
    # return True
    
    #Solution 3 -- similar to solution 2 but with less space
    for i in range(len(pureStr) // 2):
        if pureStr[i] != pureStr[len(pureStr) - 1 - i]:
            return False
    return True

# print(isPalindrome('"A man, a plan, a canal: Panama"'))