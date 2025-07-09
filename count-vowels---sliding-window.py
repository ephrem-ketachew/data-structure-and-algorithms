# 2062. Count Vowel Substrings of a String
# Easy
# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# Example 2:

# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.
# Example 3:

# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase English letters only.

from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        
        def countSubstringsWithAtMost(k):
            counter = defaultdict(int)
            left, count = None, 0
            for right in range(len(word)):
                if word[right] in vowels:
                    if left is None:
                        left = right
                    counter[word[right]] += 1
                    while len(counter) > k:
                        counter[word[left]] -= 1
                        if counter[word[left]] == 0:
                            del counter[word[left]]
                        left += 1
                        
                    count += right - left + 1
                else:
                    counter = defaultdict(int)
                    left = None
                    
            return count
        
        return countSubstringsWithAtMost(5) - countSubstringsWithAtMost(4)
    
# solution = Solution()
# word = "aeiouu"
# print(solution.countVowelSubstrings(word))