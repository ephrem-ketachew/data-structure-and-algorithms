# 2081. Sum of k-Mirror Numbers

# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

# For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
# On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.


# Example 1:

# Input: k = 2, n = 5
# Output: 25
# Explanation:
# The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#   base-10    base-2
#     1          1
#     3          11
#     5          101
#     7          111
#     9          1001
# Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
# Example 2:

# Input: k = 3, n = 7
# Output: 499
# Explanation:
# The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#   base-10    base-3
#     1          1
#     2          2
#     4          11
#     8          22
#     121        11111
#     151        12121
#     212        21212
# Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
# Example 3:

# Input: k = 7, n = 17
# Output: 20379000
# Explanation: The 17 smallest 7-mirror numbers are:
# 1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
 

# Constraints:

# 2 <= k <= 9

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def toBaseK(decimal, k):
            baseK = ''
            while decimal > 0:
                baseK = str(decimal % k) + baseK
                decimal //= k
            return baseK
        
        def isPalindrome(numStr):
            left = 0
            right = len(numStr) - 1
            while left <= right:
                if numStr[left] != numStr[right]:
                    return False
                left += 1
                right -= 1 
            return True  
    
        d = 1
        count = 0
        sum_kmirror = 0
        while count < n:
            begin = int(pow(10, d - 1))
            end = int(pow(10, d))
            for i in range(begin, end):
                s = str(i)
                s = s + s[-2::-1]
                baseK = toBaseK(int(s), k)
                if isPalindrome(baseK):
                    sum_kmirror += int(s)
                    count += 1
                    if count == n:
                        break
            if count == n:
                break
            for i in range(begin, end):
                s = str(i)
                s = s + s[::-1]
                baseK = toBaseK(int(s), k)
                if isPalindrome(baseK):
                    sum_kmirror += int(s)
                    count += 1
                    if count == n:
                        break
            d += 1
           
        return sum_kmirror
    
        # sum_kmirror = 0
        # i, count = 1, 0
        # while count < n:
        #     if isPalindrome(str(i)):
        #         baseK = toBaseK(i, k)
        #         if isPalindrome(baseK):
        #             count += 1
        #             sum_kmirror += i
        #     i += 1
        # print(i)
        # return sum_kmirror
    
    
# s = Solution()
# print(s.kMirror(5, 20))
