# 204. Count Primes
# Medium

# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

# Constraints:

# 0 <= n <= 5 * 106

class Solution:
    def countPrimes(self, n: int) -> int:
        # def is_prime(n):
        #     if n <= 1:
        #         return False
        #     if n <= 3:
        #         return True
        #     if n % 2 == 0 or n % 3 == 0:
        #         return False
            
        #     i = 5
        #     while i * i <= n:
        #         if n % i == 0 or n % (i + 2) == 0:
        #             return False
        #         i += 6
                
        #     return True
        
        # count = 0
        # for i in range(n):
        #     if is_prime(i):
        #         count += 1
                
        # return count
        
        if n <= 1:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        p = 2
        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1
            
        return sum(is_prime)