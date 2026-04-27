# 1718. Construct the Lexicographically Largest Valid Sequence
# Medium

# Given an integer n, find a sequence with elements in the range [1, n] that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

# Example 1:

# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
# Example 2:

# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
 
# Constraints:

# 1 <= n <= 20

from typing import List
from collections import Counter

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # def backtrack(curr: List[int], counter: Counter) -> List[int]:
        #     if len(curr) == 2 * n - 1:
        #         return curr[:]
            
        #     m = len(curr)
        #     for i in range(n, 0, -1):
        #         if counter[i] > 0:
        #             if i == 1 or counter[i] == 2 or (m - i >= 0 and curr[m - i] == i):
        #                 curr.append(i)
        #                 counter[i] -= 1
        #                 candidate = backtrack(curr, counter)
        #                 curr.pop()
        #                 counter[i] += 1
        #                 if candidate:
        #                     return candidate
                        
        #     return []
            
        # counter = Counter()
        # counter[1] = 1
        # for i in range(2, n + 1):
        #     counter[i] = 2
            
        # ans = backtrack([], counter)
        # return ans
        
        
        ans = [0] * (2 * n - 1)
        used = set()
        def backtrack(index: int) -> bool:
            if index == len(ans):
                return True
            
            if ans[index] != 0:
                return backtrack(index + 1)
            
            for i in range(n, 0, -1):
                if i in used:
                    continue
                
                if i == 1:
                    used.add(1)
                    ans[index] = 1
                    if backtrack(index + 1): return True
                    ans[index] = 0
                    used.remove(1)
                else:
                    if index + i < len(ans) and ans[index + i] == 0:
                        ans[index] = i
                        ans[index + i] = i
                        used.add(i)
                        if backtrack(index + 1): return True
                        ans[index] = 0
                        ans[index + i] = 0
                        used.remove(i)
                        
            return False
        
        backtrack(0)
        return ans
  
# r = Solution()  
# print(r.constructDistancedSequence(9))