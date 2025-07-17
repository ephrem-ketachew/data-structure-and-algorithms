# 2423. Remove Letter To Equalize Frequency
# Easy
# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

# Note:
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.
 
# Example 1:

# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
# Example 2:

# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

# Constraints:

# 2 <= word.length <= 100
# word consists of lowercase English letters only.

from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        
        if len(counter) == len(word):
            return True

        if len(counter) == 1:
            return True
        
        sorted_count = sorted(counter.items(), key=lambda x:x[1])
        if sorted_count[0][1] == sorted_count[-1][1]:
            return False
        
        if sorted_count[0][1] == 1 and sorted_count[1][1] == sorted_count[-1][1]:
            return True
        
        min_freq = sorted_count[0][1]
        
        count = 0
        for i in range(1, len(sorted_count)):
            count += sorted_count[i][1] - min_freq
            
            if count > 1:
                return False
            
        return True if count == 1 else False
    
    
    
# solution = Solution()
# word = "aca"
# print(solution.equalFrequency(word))