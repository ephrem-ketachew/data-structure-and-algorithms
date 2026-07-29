# 3518. Smallest Palindromic Rearrangement II
# Hard

# You are given a palindromic string s and an integer k.

# Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

# Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

# Example 1:

# Input: s = "abba", k = 2

# Output: "baab"

# Explanation:

# The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
# Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
# Example 2:

# Input: s = "aa", k = 2

# Output: ""

# Explanation:

# There is only one palindromic rearrangement: "aa".
# The output is an empty string since k = 2 exceeds the number of possible rearrangements.
# Example 3:

# Input: s = "bacab", k = 1

# Output: "abcba"

# Explanation:

# The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
# Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.
# 1 <= k <= 106

from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counter = Counter(s)
        half = [0] * 26
        mid_char = ''
        for char, freq in counter.items():
            if freq % 2 == 1:
                mid_char = char
            half[ord(char) - 97] = freq // 2
            
        P = 1
        total = sum(half)
        rem = total
        for i in range(26):
            if half[i] != 0:
                P *= comb(rem, half[i])
                rem -= half[i]
                
        if k > P:
            return ''
        
        ans = []
        rem = total
        for _ in range(total):
            for i in range(26):
                if half[i] > 0:
                    branch_perm = P * half[i] // rem
                    if k <= branch_perm:
                        ans.append(chr(i + 97))
                        P = branch_perm
                        half[i] -= 1
                        rem -= 1
                        break
                    else:
                        k -= branch_perm
                   
        first_half = ''.join(ans) 
        return first_half + mid_char + first_half[::-1]