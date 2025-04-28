# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a

from collections import Counter

def lengthOfLongestSubstring(s):
    left = 0
    max_length = 0
    
    window_counter = Counter()
    
    for right in range(len(s)):
        window_counter[s[right]] += 1
        
        while window_counter[s[right]] > 1:
            window_counter[s[left]] -= 1
            if window_counter[s[left]] == 0:
                del window_counter[s[left]]
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

print(lengthOfLongestSubstring("pwwkew"))