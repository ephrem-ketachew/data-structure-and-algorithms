def isPalindrome(x):
    x = str(x)
    for i in range(len(x)// 2):
        if not x[i]== x[len(x)- 1 - i]:
            return False
    return True