# 541. Reverse String II
# Easy
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # def reverse(index):
        #     left = index
        #     right = index + k - 1 if index + k - 1 < len(s) else len(s) - 1
        #     while left < right:
        #         res[left], res[right] = res[right], res[left]
        #         left += 1
        #         right -= 1
            
        res = list(s)
        # for i in range(len(s)):
        #     if i % (2 * k ) == 0:
        #         reverse(i)
        
        for i in range(0, len(res), 2 * k):
            res[i:i+k] = reversed(res[i:i+k])
                
        return ''.join(res)
    
solution = Solution()
s = "abcdefg"
k = 2
s = "abcd"
k = 2
print(solution.reverseStr(s, k))