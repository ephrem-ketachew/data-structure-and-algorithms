# 3234. Count the Number of Substrings With Dominant Ones
# Medium
# You are given a binary string s.

# Return the number of substrings with dominant ones.

# A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

# Example 1:

# Input: s = "00011"

# Output: 5

# Explanation:

# The substrings with dominant ones are shown in the table below.

# i	j	s[i..j]	Number of Zeros	Number of Ones
# 3	3	1	0	1
# 4	4	1	0	1
# 2	3	01	1	1
# 3	4	11	0	2
# 2	4	011	1	2
# Example 2:

# Input: s = "101101"

# Output: 16

# Explanation:

# The substrings with non-dominant ones are shown in the table below.

# Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

# i	j	s[i..j]	Number of Zeros	Number of Ones
# 1	1	0	1	0
# 4	4	0	1	0
# 1	4	0110	2	2
# 0	4	10110	2	3
# 1	5	01101	2	3
 
# Constraints:

# 1 <= s.length <= 4 * 104
# s consists only of characters '0' and '1'.

from math import sqrt

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # CHAPTER ONE 
        # IGNORANCE LEADS TO BRUTE FORCE ... TLE
        
        # count = 0
        # ones = 0
        # zeros = 0
        
        # for right in range(len(s)):
        #     for left in range(right, -1, -1):
        #         if s[left] == '1':
        #             ones += 1
        #         else:
        #             zeros += 1
                
        #         if ones >= zeros * zeros:
        #             count += 1
                    
        #         if zeros * zeros > ones + left:
        #             break
                    
        #     zeros = ones = 0
                    
        # return count
        
        # CHAPTER TWO 
        # I GAVE UP SEARCH FOR THE SOLUTION AND WHEN FOUND TOOK ME 5 HOURS TO UNDERSTAND IT
        # BRAINCELLS DIED😭😭😭😭😭
        # THE HARDEST QUESTION I HAVE EVER MET
        # THE GREATES BETRYAL OF THE 21ST CETNTURY -- LEETCODE AIN'T HAD SHAME TAGGING THIS QUESTION MEDIUM, EVEN WORSE SLIDING WINDOW
        # MY DAY RUINED .... A TOTAL OF 7 HOURS WASTED ON A SINGLE QUESTION.... I HAVE NEVER EVER DONE THIS BEFORE
        # NOW I UNDERSTAND IT AND CODED AND BLOODY AC FROM LEETCODE..... HOURS OF IGNORANCE, SWEAT, BLOOD, BONE, ....
        # CHATGPT, GEMINI, DEEPSEEK ... ALL OF THEM COUND'T SOLVE .... ONLY GEMINI 2.5 PRO WAS ABLE TO SOLVE IT
        
        ans = 0
        n = len(s)
        
        count_ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_ones += 1
            else:
                ans += count_ones * (1 + count_ones) // 2
                count_ones = 0
                
        ans += count_ones * (1 + count_ones) // 2
        
        zero_indices = [-1] + [index for index, char in enumerate(s) if char == '0'] + [n]
        
        if len(zero_indices) - 2 == 0:
            return ans
        
        max_zeros = int(sqrt(n))
        
        for zero_count in range(1, max_zeros + 1):
            if zero_count > len(zero_indices) - 2:
                break
            
            for zero_index in range(1, len(zero_indices) - zero_count):
                start_index = zero_indices[zero_index]
                end_index = zero_indices[zero_index + zero_count - 1]
                
                left_ones = start_index - zero_indices[zero_index - 1] - 1
                right_ones = zero_indices[zero_index + zero_count] - end_index - 1
                middle_ones = end_index - start_index + 1 - zero_count
                
                required_ones = max(zero_count ** 2 - middle_ones, 0)
                available_ones = left_ones + right_ones
                
                if available_ones < required_ones:
                    continue
                
                local_ans = 0
                
                if required_ones <= left_ones:
                    local_ans += (left_ones - required_ones + 1) * (right_ones + 1)
                    
                left_ones_min = max(0, required_ones - right_ones)
                left_ones_max = min(left_ones, required_ones - 1)
                
                if left_ones_min <= left_ones_max:
                    left_ones_count = left_ones_max - left_ones_min + 1
                    
                    local_ans += left_ones_count * (right_ones - required_ones + 1)
                    local_ans += left_ones_count * (left_ones_min + left_ones_max) // 2
                    
                ans += local_ans
                    
        return ans
        
        
        
    
# solution = Solution()
# s = "00011"
# s = "101101"
# print(solution.numberOfSubstrings(s))