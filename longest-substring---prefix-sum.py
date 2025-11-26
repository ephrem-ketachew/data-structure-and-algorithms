# 1371. Find the Longest Substring Containing Vowels in Even Counts
# Medium

# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

# Example 1:

# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
# Example 2:

# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# Example 3:

# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 
# Constraints:

# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        parity = [0] * 5
        seen = {tuple(parity):-1}
        max_len = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                idx = vowels[ch]
                parity[idx] ^= 1
                
            if tuple(parity) in seen:
                max_len = max(max_len, i - seen[tuple(parity)])
            else:
                seen[tuple(parity)] = i
                
        return max_len