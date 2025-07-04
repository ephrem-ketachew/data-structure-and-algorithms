# 3258. Count Substrings That Satisfy K-Constraint I
# Easy
# You are given a binary string s and an integer k.

# A binary string satisfies the k-constraint if either of the following conditions holds:

# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.

# Example 1:

# Input: s = "10101", k = 1

# Output: 12

# Explanation:

# Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

# Example 2:

# Input: s = "1010101", k = 2

# Output: 25

# Explanation:

# Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.

# Example 3:

# Input: s = "11111", k = 1

# Output: 15

# Explanation:

# All substrings of s satisfy the k-constraint.

# Constraints:

# 1 <= s.length <= 50 
# 1 <= k <= s.length
# s[i] is either '0' or '1'.

from collections import Counter

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        count = 0
        window_counter = Counter()
        
        for right in range(len(s)):
            window_counter[s[right]] += 1
            while window_counter['0'] > k and window_counter['1'] > k:
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
                left += 1
            
            count += right - left + 1
            
        return count
    
# solution = Solution()
# s = "10101"
# k = 1
# print(solution.countKConstraintSubstrings(s, k))