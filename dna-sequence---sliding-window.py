# 187. Repeated DNA Sequences
# Medium
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seen = set()
        output = set()
        
        for i in range(10, len(s) + 1):
            sub = s[i - 10:i]
            if sub in seen:
                output.add(sub)
            else: 
                seen.add(sub)
        
        return list(output)
    
# solution = Solution()
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"
# s = "AAAAAAAAAAA"
# print(solution.findRepeatedDnaSequences(s))