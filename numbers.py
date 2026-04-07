# 386. Lexicographical Numbers
# Medium

# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:

# Input: n = 2
# Output: [1,2]
 
# Constraints:

# 1 <= n <= 5 * 104

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # self.ans = []
        # def dfs(built: list[str]) -> None:
        #     for i in range(10):
        #         if i == 0 and not built:
        #             continue
                    
        #         cur_built = built + [str(i)]
        #         cur_num = int(''.join(cur_built))
        #         if cur_num <= n:
        #             self.ans.append(cur_num)
        #             dfs(cur_built)
        #         else:
        #             break
        
        # dfs([])
        
        # return self.ans
        
        ans = []
        cur = 1
        for _ in range(n):
            ans.append(cur)
            
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur >= n or cur % 10 == 9:
                    cur //= 10
                    
                cur += 1
                
        return ans