# 1898. Maximum Number of Removable Characters
# Medium
# You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

# You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

# Return the maximum k you can choose such that p is still a subsequence of s after the removals.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# Example 1:

# Input: s = "abcacb", p = "ab", removable = [3,1,0]
# Output: 2
# Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
# "ab" is a subsequence of "accb".
# If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
# Hence, the maximum k is 2.
# Example 2:

# Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
# Output: 1
# Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
# "abcd" is a subsequence of "abcddddd".
# Example 3:

# Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
# Output: 0
# Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.

# Constraints:

# 1 <= p.length <= s.length <= 105
# 0 <= removable.length < s.length
# 0 <= removable[i] < s.length
# p is a subsequence of s.
# s and p both consist of lowercase English letters.
# The elements in removable are distinct.

from typing import List
# from collections import defaultdict
# import bisect

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # index_map = defaultdict(list)
        # for idx, ch in enumerate(s):
        #     index_map[ch].append(idx)
          
        # k = 0  
        # for index in removable:
        #     index_map[s[index]].remove(index)
            
        #     last_idx = -1
        #     for char in p:
        #         idx = bisect.bisect_right(index_map[char], last_idx)
        #         if idx == len(index_map[char]):
        #             return k
        #         last_idx = index_map[char][idx]
            
        #     k += 1
            
        # return k
        
        # def is_subsequence(p, s, removed):
        #     n, m = len(p), len(s)
        #     i, j = 0, 0
            
        #     while i < n and j < m:
        #         if not removed[j] and s[j] == p[i]:
        #             i += 1
        #         j += 1
                
        #     return i == n
            
        
        # left, right = 0, len(removable) - 1
        # removed = [False] * len(s)
        # k = 0
        # while left <= right:
        #     mid = (left + right) // 2
        #     for i in range(0, mid + 1):
        #         removed[removable[i]] = True
                
        #     if is_subsequence(p, s, removed):
        #         k = max(k, mid) + 1
        #         left = mid + 1
        #     else:
        #         right = mid - 1
              
        #     for i in range(0, mid + 1):
        #          removed[removable[i]] = False
            
            
        # return k
        
        # def is_subsequence(k):
        #     removed = set(removable[:k])
        #     i = j = 0
        #     while i < len(p) and j < len(s):
        #         if j not in removed and s[j] == p[i]:
        #             i += 1
        #         j += 1
                
        #     return i == len(p)
        
        # left, right, ans = 0, len(removable), 0
        # while left <= right:
        #     mid = (left + right) // 2
        #     if is_subsequence(mid):
        #         ans = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
                
        # return ans
        
        pos = [float('inf')] * len(s)
        for step, idx in enumerate(removable):
            pos[idx] = step
         
        def is_subsequence(k):
            i = j = 0
            while i < len(p) and j < len(s):
                if pos[j] >= k and s[j] == p[i]:
                    i += 1
                j += 1
                
            return i == len(p)
        
        left, right, ans = 0, len(removable), 0
        while left <= right:
            mid = (left + right) // 2
            if is_subsequence(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
    
# solution = Solution()
# s = "abcbddddd"
# p = "abcd"
# removable = [3,2,1,4,5,6]
# s = "abcab" 
# p = "abc"
# removable = [0,1,2,3,4]
# s = "abcacb"
# p = "ab"
# removable = [3,1,0]
# s = "kkwiypfzruadoeyfzogmpslfbvrumcrogouomuaidyhqvlaumguqcipcbfkdnp"
# p = "kkiyaogslrroadmcb"
# removable = [52,44,9,12,54,5,16,36,23,8,43,58,15,13,28,2,29,27,34,60,25,35,20,7,31,11,51,39,19,24,21,38,42,57,49,37,59,50]
# print(solution.maximumRemovals(s, p, removable))