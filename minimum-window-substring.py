# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from collections import Counter 

def min_window(s: str, t: str) -> str:
    t_counter = Counter(t)
    window_counter = Counter()
    left = 0
    min_length = float('inf')
    left_index = -1
    right_index = -1
    
    if len(s) < len(t):
        return ''
    
    for right in range(len(s)):
        window_counter[s[right]] += 1
                
        while left < len(s) and (s[left] not in t_counter or window_counter[s[left]] > t_counter[s[left]]):
            window_counter[s[left]] -= 1
            if window_counter[s[left]] == 0:
                del window_counter[s[left]]
            left += 1
                
        if window_counter >= t_counter:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                left_index = left
                right_index = right
        
    return s[left_index:right_index + 1]
                