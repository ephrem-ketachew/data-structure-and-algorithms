# 2024. Maximize the Confusion of an Exam
# Medium
# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

# Example 1:

# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.
# Example 2:

# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.
# Example 3:

# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
# In both cases, there are five consecutive 'T's.

# Constraints:

# n == answerKey.length
# 1 <= n <= 5 * 104
# answerKey[i] is either 'T' or 'F'
# 1 <= k <= n

from collections import Counter

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # left = 0
        # max_len = 0
        # counter = Counter()
        
        # for right in range(len(answerKey)):
        #     counter[answerKey[right]] += 1
            
        #     while counter['T'] > k and counter['F'] > k:
        #         counter[answerKey[left]] -= 1
        #         if counter[answerKey[left]] == 0:
        #             del counter[answerKey[left]]
        #         left += 1
                
        #     max_len = max(max_len, right - left + 1)
            
        # return max_len
        
        left, count_true, count_false, max_len = 0, 0, 0, 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                count_true += 1
            else:
                count_false += 1
            
            while count_true > k and count_false > k:
                if answerKey[left] == 'T':
                    count_true -= 1
                else:
                    count_false -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
    
# answerKey = "TTFF"
# k = 2
# answerKey = "TFFT"
# k = 1
# answerKey = "TTFTTFTT"
# k = 1
# solution = Solution()
# print(solution.maxConsecutiveAnswers(answerKey, k))