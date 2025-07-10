# 1358. Number of Substrings Containing All Three Characters
# Medium
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.

from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = defaultdict(int)
        count, left = 0, 0
        
        for right in range(len(s)):
            counter[s[right]] += 1
            while counter['a'] >= 1 and counter['b'] >= 1 and counter['c'] >= 1:
            # while all(counter[ch] >= 1 for ch in 'abc'):
                counter[s[left]] -= 1
                left += 1
            count += left
                
        return count
    
# solution = Solution()
# s = "abcabc"
# print(solution.numberOfSubstrings(s))