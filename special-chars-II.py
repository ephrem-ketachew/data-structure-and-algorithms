# 3121. Count the Number of Special Characters II
# Medium

# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

# Return the number of special letters in word.

# Example 1:

# Input: word = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters are 'a', 'b', and 'c'.

# Example 2:

# Input: word = "abc"

# Output: 0

# Explanation:

# There are no special characters in word.

# Example 3:

# Input: word = "AbBCab"

# Output: 0

# Explanation:

# There are no special characters in word.

# Constraints:

# 1 <= word.length <= 2 * 105
# word consists of only lowercase and uppercase English letters.

from collections import Counter

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = Counter(word)
        cur_low_counter = Counter()
        seen = set()
        count = 0
        for ch in word:
            if ch.isupper() and ch not in seen and cur_low_counter[ch.lower()] == counter[ch.lower()] > 0:
                count += 1
            if ch.islower():
                cur_low_counter[ch] += 1
            else:
                seen.add(ch)
        
        return count