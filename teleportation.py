# 3629. Minimum Jumps to Reach End via Prime Teleportation
# Medium

# You are given an integer array nums of length n.

# You start at index 0, and your goal is to reach index n - 1.

# From any index i, you may perform one of the following operations:

# Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
# Return the minimum number of jumps required to reach index n - 1.

# Example 1:

# Input: nums = [1,2,4,6]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index 1.
# At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
# Thus, the answer is 2.

# Example 2:

# Input: nums = [2,3,4,7,9]

# Output: 2

# Explanation:

# One optimal sequence of jumps is:

# Start at index i = 0. Take an adjacent step to index i = 1.
# At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
# Thus, the answer is 2.

# Example 3:

# Input: nums = [4,6,5,8]

# Output: 3

# Explanation:

# Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

# Constraints:

# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 106

from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        max_num = max(nums)
        if max_num < 2:
            return n - 1
        
        spf = list(range(max_num + 1))
        for prime in range(2, int(max_num ** 0.5) + 1):
            if spf[prime] == prime:
                for multiple in range(prime, max_num + 1, prime):
                    if spf[multiple] == multiple:
                        spf[multiple] = prime
                    
                    
        def is_prime(num: int) -> bool:
            return num >= 2 and spf[num] == num
        
        prime_teleport = defaultdict(list)
        for i, num in enumerate(nums):
            curr = num
            while curr > 1:
                p = spf[curr]
                prime_teleport[p].append(i)
                while curr % p == 0:
                    curr //= p
                    
        visited_idx = [False] * n
        visited_idx[0] = True
        
        queue = deque([0])
        visited_primes = set()
        steps = 0
        while queue:
            t = len(queue)
            for _ in range(t):
                idx = queue.popleft()
                if idx == n - 1:
                    return steps
                
                for nxt in (idx - 1, idx + 1):
                    if 0 <= nxt < n and not visited_idx[nxt]:
                        visited_idx[nxt] = True
                        queue.append(nxt)
                        
                num = nums[idx]
                if is_prime(num) and num not in visited_primes:
                    visited_primes.add(num)
                    for i in prime_teleport[num]:
                        if not visited_idx[i]:
                            visited_idx[i] = True
                            queue.append(i)
                            
            steps += 1
            
        return "Whatever I want :)"

            
        
        
        # FAILED ATTEMPT
        # def prime_factors(num: int) -> List[int]:
        #     factors = []
        #     if num % 2 == 0:
        #         factors.append(2)
        #         while num % 2 == 0:
        #             num //= 2
                    
        #     divisor = 3
        #     while divisor * divisor <= num:
        #         if num % divisor == 0:
        #             factors.append(divisor)
        #             while num % divisor == 0:
        #                 num //= divisor
        #         divisor += 2
                
        #     if num > 1:
        #         factors.append(num)
                
        #     return factors
        
        # teleport = defaultdict(int)
        # for i, num in enumerate(nums):
        #     factors = prime_factors(num)
        #     for prime in factors:
        #         teleport[prime] = i
     
        # n = len(nums)
        # min_jumps = n - 1
        # for i, num in enumerate(nums):
        #     jumps = n - 1 - (teleport[num] - i - 1)
        #     min_jumps = min(min_jumps, jumps)
            
        # return min_jumps