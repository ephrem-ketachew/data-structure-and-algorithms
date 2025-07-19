# 2982. Find Longest Special Substring That Occurs Thrice II
# Medium

# You are given a string s that consists of lowercase English letters.

# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "aaaa"
# Output: 2
# Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
# It can be shown that the maximum length achievable is 2.
# Example 2:

# Input: s = "abcdef"
# Output: -1
# Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
# Example 3:

# Input: s = "abcaba"
# Output: 1
# Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
# It can be shown that the maximum length achievable is 1.
 
# Constraints:

# 3 <= s.length <= 5 * 105
# s consists of only lowercase English letters.
from collections import defaultdict
import heapq

class Solution:
    def maximumLength(self, s: str) -> int:
        # counter = defaultdict(int)
        # left = 0
        # max_len = -1
        # count = 1
        
        # s += 'A'
        
        # for right in range(len(s)):
        #     while s[left] != s[right]:
        #         sub = s[left: right]
        #         counter[sub] += count
        #         if counter[sub] >= 3:
        #             max_len = max(max_len, right - left)
        #         left += 1
        #         count += 1
        #     count = 1
                
        # return max_len
    
        # 😭Memory Limit Exceeded "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..."
        # 868 / 906 testcases passed
        
        counter = defaultdict(list)
        left = 0
        max_len = -1
        count = 0
        
        s += 'A'
        
        for right in range(len(s)):
            if s[right] != s[left]:
                cur_len = right - left
                ch = s[left]
                for k in range(cur_len, 0, -1):
                    if len(counter[ch]) < 3:
                        heapq.heappush(counter[ch], k)
                    else:
                        heapq.heappushpop(counter[ch], k)
                    count += 1

                    if count == 3:
                        break
                    
                left = right
                count = 0
                
        for ch in counter:
            if len(counter[ch]) == 3:
                max_len = max(max_len, counter[ch][0])
                
        return max_len
    
    
# solution = Solution()
# s = "aaaa"
# s = "abcdef"
# s = "abcaba"
# print(solution.maximumLength(s))
        
        
        
        