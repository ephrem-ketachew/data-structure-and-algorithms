# 1078. Occurrences After Bigram
# Easy
# Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

# Return an array of all the words third for each occurrence of "first second third".

# Example 1:

# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]
# Example 2:

# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]

# Constraints:

# 1 <= text.length <= 1000
# text consists of lowercase English letters and spaces.
# All the words in text are separated by a single space.
# 1 <= first.length, second.length <= 10
# first and second consist of lowercase English letters.
# text will not have any leading or trailing spaces.

from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(' ')
        
        if len(words) < 3:
            return []
        
        ans = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
                
        return ans
        
# solution = Solution()
# text = "alice is a good girl she is a good student"
# first = "a"
# second = "good"
# print(solution.findOcurrences(text, first, second))