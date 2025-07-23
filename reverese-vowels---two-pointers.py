# 345. Reverse Vowels of a String
# Easy
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        left, right = 0, len(s) - 1
        
        s_list = list(s)
        while left < right:
            while left < len(s_list) and s_list[left] not in vowels:
                left += 1
                
            while right >= 0 and s_list[right] not in vowels:
                right -= 1
                
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                
            left += 1
            right -= 1
                
        return ''.join(s_list)
        