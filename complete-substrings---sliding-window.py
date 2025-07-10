# 2953. Count Complete Substrings
# Hard
# You are given a string word and an integer k.

# A substring s of word is complete if:

# Each character in s occurs exactly k times.
# The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
# Return the number of complete substrings of word.

# A substring is a non-empty contiguous sequence of characters in a string.

# Example 1:

# Input: word = "igigee", k = 2
# Output: 3
# Explanation: The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: igigee, igigee, igigee.
# Example 2:

# Input: word = "aaabbbccc", k = 3
# Output: 6
# Explanation: The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc.
 
# Constraints:

# 1 <= word.length <= 105
# word consists only of lowercase English letters.
# 1 <= k <= word.length

from collections import defaultdict

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def __count_in_chunks(chunk):
            chunk_len = len(chunk)
            count = 0
            
            for unique_char_count in range(1, 27):
                win_len = unique_char_count * k
                
                if chunk_len < win_len:
                    break
                
                counter = defaultdict(int)
                good_chars = 0
                
                for i in range(win_len):
                    if counter[chunk[i]] == k:
                        good_chars -= 1
                    counter[chunk[i]] += 1
                    if counter[chunk[i]] == k:
                        good_chars += 1
                        
                if unique_char_count == good_chars and len(counter) == unique_char_count:
                    count += 1
                    
                for i in range(win_len, chunk_len):
                    if counter[chunk[i]] == k:
                        good_chars -= 1
                    counter[chunk[i]] += 1
                    if counter[chunk[i]] == k:
                        good_chars += 1
                        
                    if counter[chunk[i - win_len]] == k:
                        good_chars -= 1
                    counter[chunk[i - win_len]] -= 1
                    if counter[chunk[i - win_len]] == k:
                        good_chars += 1
                        
                    if counter[chunk[i - win_len]] == 0:
                        del counter[chunk[i - win_len]]
                        
                    if unique_char_count == good_chars and len(counter) == unique_char_count:
                        count += 1
                        
            return count
        
        count = 0
        start = 0
        for i in range(len(word)):
            if i > 0 and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                count += __count_in_chunks(word[start:i])
                start = i
                
        count += __count_in_chunks(word[start:])
                
        return count
            
        
        # WRONG ASSUMPTION WRONG APPROACH WRONG CODE --- FIRST TRY
        # def substrings_at_most_k(k):
        #     counter = defaultdict(int)
        #     left, count = 0, 0
            
        #     for right in range(len(word)):
        #         counter[word[right]] += 1
        #         if right > 0 and abs(ord(word[right]) - ord(word[right - 1])) > 2:
        #             left = right
        #             counter = defaultdict(int)
        #         while counter[word[right]] > k:
        #             counter[word[left]] -= 1
        #             if counter[word[left]] == 0:
        #                 del counter[word[left]]
        #             left += 1
                
        #         count += right - left + 1

        #     return count
        
        # return substrings_at_most_k(k) - substrings_at_most_k(k - 1)
    
# solution = Solution()
# word = "igigee"
# k = 2
# print(solution.countCompleteSubstrings(word, k))