# 3714. Longest Balanced Substring II
# Medium

# You are given a string s consisting only of the characters 'a', 'b', and 'c'.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "aabcc"

# Output: 3

# Explanation:

# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

# Constraints:

# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        
        cur_len = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        max_len = max(max_len, cur_len)
                
        def balanced_two_chars(first_char: 'str', second_char: 'str', ignore_char: 'str') -> None:
            nonlocal max_len
            seen = {0: -1}
            prefix = 0
            for i, ch in enumerate(s):
                if ch == ignore_char:
                    seen = {0: i}
                    prefix = 0
                else:
                    if ch == first_char:
                        prefix += 1
                    else:
                        prefix -= 1
                        
                    if prefix in seen:
                        max_len = max(max_len, i - seen[prefix])
                    else:
                        seen[prefix] = i
                        
        balanced_two_chars('a', 'b', 'c')
        balanced_two_chars('a', 'c', 'b')
        balanced_two_chars('b', 'c', 'a')
        seen = {(0, 0): -1}
        count_a = count_b = count_c = 0
        for i, ch in enumerate(s):
            if ch == 'a': count_a += 1
            if ch == 'b': count_b += 1
            if ch == 'c': count_c += 1
            
            state = (count_a - count_b, count_a - count_c)
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i
                
        return max_len
                