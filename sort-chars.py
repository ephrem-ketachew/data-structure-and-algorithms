# 451. Sort Characters By Frequency
# Medium

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # counter = Counter(s)
        # return ''.join(sorted(s, key=lambda x:(counter[x], x), reverse=True))
        
        counter = Counter(s)
        max_freq = max(counter.values())
        
        buckets = [[] for i in range(max_freq + 1)]
        
        for char, freq in counter.items():
            buckets[freq].append(char)
            
        ans = []
        for freq in range(len(buckets) - 1, 0, -1):
            for char in buckets[freq]:
                ans.append(char * freq)
                
        return ''.join(ans)
    
    
# solution = Solution()
# s = "loveleetcode"
# print(solution.frequencySort(s))