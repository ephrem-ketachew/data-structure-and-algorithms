# 3298. Count Substrings That Can Be Rearranged to Contain a String II
# Hard
# You are given two strings word1 and word2.

# A string x is called valid if x can be rearranged to have word2 as a prefix.

# Return the total number of valid substrings of word1.

# Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.

# Example 1:

# Input: word1 = "bcca", word2 = "abc"

# Output: 1

# Explanation:

# The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.

# Example 2:

# Input: word1 = "abcabc", word2 = "abc"

# Output: 10

# Explanation:

# All the substrings except substrings of size 1 and size 2 are valid.

# Example 3:

# Input: word1 = "abcabc", word2 = "aaabc"

# Output: 0

# Constraints:

# 1 <= word1.length <= 106
# 1 <= word2.length <= 104
# word1 and word2 consist only of lowercase English letters.

from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        counter2 = Counter(word2)
        win_counter = Counter()
        
        required = len(counter2)
        count = formed = left = 0
        
        for right in range(len(word1)):
            ch = word1[right]
            win_counter[ch] += 1
            
            if win_counter[ch] == counter2[ch]:
                formed += 1
                
            while formed == required:
                ch = word1[left]
                
                if win_counter[ch] == counter2[ch]:
                    formed -= 1
                    
                win_counter[ch] -= 1
                if win_counter[ch] == 0:
                    del win_counter[ch]
                
                left += 1
                    
            count += left
            
        return count
    