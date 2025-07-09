# 2531. Make Number of Distinct Characters Equal
# Medium
# You are given two 0-indexed strings word1 and word2.

# A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

# Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

# Example 1:

# Input: word1 = "ac", word2 = "b"
# Output: false
# Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
# Example 2:

# Input: word1 = "abcc", word2 = "aab"
# Output: true
# Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
# Example 3:

# Input: word1 = "abcde", word2 = "fghij"
# Output: true
# Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 consist of only lowercase English letters.

from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # def __is_it_possible(counter1, counter2):
        #     if len(counter1) - len(counter2) == 1:
        #         for char in counter1:
        #             if counter1[char] > 1 and char not in counter2:
        #                 for c in counter2:
        #                     if c in counter1 and counter2[c] > 1:
        #                         return True
                            
        #             elif counter1[char] == 1:
        #                 if char not in counter2:
        #                     for c in counter2:
        #                         if c in counter1 and counter2[c] == 1:
        #                             return True
        #                 else:
        #                     for c in counter2:
        #                         if c != char and c in counter1 and counter2[c] > 1:
        #                             return True
        #         return False
        #     else:
        #         for char in counter1:
        #             if counter1[char] == 1 and char not in counter2:
        #                 for c in counter2:
        #                     if c in counter1 and counter2[c] > 1:
        #                         return True
        #         return False
            
        # word1_counter = Counter(word1)
        # word2_counter = Counter(word2)
        
        # if abs(len(word1_counter) - len(word2_counter)) == 0:
        #     for char in word1_counter:
        #         if char in word2_counter:
        #             return True
        #         elif word1_counter[char] == 1:
        #             if 1 in word2_counter.values():
        #                 return True
        #         else:
        #             for c in word2_counter:
        #                 if word2_counter[c] > 1 and c not in word1_counter:
        #                     return True
        #     return False
        
        # if abs(len(word1_counter) - len(word2_counter)) > 2:
        #     return False
        
        # if len(word1_counter) > len(word2_counter):
        #     return __is_it_possible(word1_counter, word2_counter)
        # else:
        #     return __is_it_possible(word2_counter, word1_counter)
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        for char1 in counter1:
            for char2 in counter2:
                if char1 == char2:
                    if len(counter1) == len(counter2):
                        return True
                    continue
                
                count1 = counter1.copy()
                count2 = counter2.copy()
                
                count1[char1] -= 1
                if count1[char1] == 0:
                    del count1[char1]
                if char1 not in count2:
                    count2[char1] += 1
                    
                count2[char2] -= 1
                if count2[char2] == 0:
                    del count2[char2]
                if char2 not in count1:
                    count1[char2] += 1
                    
                if len(count1) == len(count2):
                    return True
                
        return False