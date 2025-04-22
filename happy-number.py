def isHappy(n):
    def getNewNumber(n):
        sumOfDigits = 0
        while n > 0:
            digit = n % 10
            sumOfDigits += digit * digit
            n //= 10
        return sumOfDigits
    
    #The following loop worked fine(beats 100% with 0ms on leetcode - but itsn't readable...one can't tell for sure that all unhappy numbers would fall below 10)
    # while n == 7 or n > 9:
    #     n = getNewNumber(n)

    #so the need to write the following piece of code 
    seen = set()

    while n != 1:
        n = getNewNumber(n)
        if n in seen:
            return False
        seen.add(n)
    
    return n == 1
 