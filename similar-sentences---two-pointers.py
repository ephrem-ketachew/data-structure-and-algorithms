# 1813. Sentence Similarity III
# Medium
# You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

# Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

# For example,

# s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
# s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.
# Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

# Example 1:

# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

# Output: true

# Explanation:

# sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

# Example 2:

# Input: sentence1 = "of", sentence2 = "A lot of words"

# Output: false

# Explanation:

# No single sentence can be inserted inside one of the sentences to make it equal to the other.

# Example 3:

# Input: sentence1 = "Eating right now", sentence2 = "Eating"

# Output: true

# Explanation:

# sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

# Constraints:

# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
# The words in sentence1 and sentence2 are separated by a single space.

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
            
        j = 0
        while j < len(s1) - i and s1[-1 - j] == s2[-1 - j]:
            j += 1
            
        return i + j == len(s1)
        
        
        # CHAPTER ONE = ABSOLUTE WRONG APPROACH 
        # I WAS HERE ONLY TO WASTE MY TIME AND OF COURSE TO LOWER THE ACCEPTANCE RATE OF THE QUESTION😭😅
        # def is_similar(s1, s2):
        #     i = j = 0
        #     count = 0
        #     while i < len(s1) and j < len(s2):
        #         if s1[i] != s2[j]:
        #             count += 1
        #             while j < len(s2) and s1[i] != s2[j]:
        #                 j += 1
                    
        #         if j < len(s2):
        #             i += 1
        #             j += 1
                    
        #     if i == len(s1) and len(s2[j:]) > 0:
        #         count += 1
                
        #     return i == len(s1) and count <= 1
        
        # sentence1 = sentence1.split()
        # sentence2 = sentence2.split()
        
        # return is_similar(sentence1, sentence2) or is_similar(sentence2, sentence1)
    
    
# solution = Solution()
# sentence1 = "My name is Haley"
# sentence2 = "My Haley"
# sentence1 = "of"
# sentence2 = "A lot of words"
# sentence1 = "Eating right now"
# sentence2 = "Eating"
# sentence1 = "Ogn WtWj HneS"
# sentence2 = "Ogn WtWj HneS"
# print(solution.areSentencesSimilar(sentence1, sentence2))