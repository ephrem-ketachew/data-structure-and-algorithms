# 3306. Count of Substrings Containing Every Vowel and K Consonants II
# Medium

# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

# Example 1:

# Input: word = "aeioqq", k = 1

# Output: 0

# Explanation:

# There is no substring with every vowel.

# Example 2:

# Input: word = "aeiou", k = 0

# Output: 1

# Explanation:

# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:

# Input: word = "ieaouqqieaouqq", k = 1

# Output: 3

# Explanation:

# The substrings with every vowel and one consonant are:

# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".

# Constraints:

# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5

from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        def count_at_most_k(k):
            vowel_counter = defaultdict(int)
            consonant_count = 0
            start = count = left = 0   
            for right in range(len(word)):
                ch = word[right]
                if ch in vowels:
                    vowel_counter[ch] += 1
                else:
                    consonant_count += 1
     
                while left <= right and consonant_count > k:
                    ch = word[left]
                    
                    if ch in vowels:
                        if left >= start:
                            vowel_counter[ch] -= 1
                            if vowel_counter[ch] == 0:
                                del vowel_counter[ch]
                    else:
                        consonant_count -= 1
                            
                    left += 1
                         
                start = max(start, left)
                
                while len(vowel_counter) == 5:
                    ch = word[start]
                    if ch in vowels:
                        if vowel_counter[ch] == 1:
                            break
                        vowel_counter[ch] -= 1

                    start += 1

                if len(vowel_counter) == 5:
                    count += start - left + 1

            return count
     
        return count_at_most_k(k) - count_at_most_k(k - 1) if k > 0 else count_at_most_k(0)
    
    