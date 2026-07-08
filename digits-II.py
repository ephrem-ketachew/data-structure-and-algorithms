# 3756. Concatenate Non-Zero Digits and Multiply by Sum II
# Medium

# You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

# For each queries[i], extract the substring s[li..ri]. Then, perform the following:

# Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
# Let sum be the sum of digits in x. The answer is x * sum.
# Return an array of integers answer where answer[i] is the answer to the ith query.

# Since the answers may be very large, return them modulo 109 + 7.

# Example 1:

# Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]

# Output: [12340, 4, 9]

# Explanation:

# s[0..7] = "10203004"
# x = 1234
# sum = 1 + 2 + 3 + 4 = 10
# Therefore, answer is 1234 * 10 = 12340.
# s[1..3] = "020"
# x = 2
# sum = 2
# Therefore, the answer is 2 * 2 = 4.
# s[4..6] = "300"
# x = 3
# sum = 3
# Therefore, the answer is 3 * 3 = 9.
# Example 2:

# Input: s = "1000", queries = [[0,3],[1,1]]

# Output: [1, 0]

# Explanation:

# s[0..3] = "1000"
# x = 1
# sum = 1
# Therefore, the answer is 1 * 1 = 1.
# s[1..1] = "0"
# x = 0
# sum = 0
# Therefore, the answer is 0 * 0 = 0.
# Example 3:

# Input: s = "9876543210", queries = [[0,9]]

# Output: [444444137]

# Explanation:

# s[0..9] = "9876543210"
# x = 987654321
# sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
# Therefore, the answer is 987654321 * 45 = 44444444445.
# We return 44444444445 modulo (109 + 7) = 444444137.

# Constraints:

# 1 <= m == s.length <= 105
# s consists of digits only.
# 1 <= queries.length <= 105
# queries[i] = [li, ri]
# 0 <= li <= ri < m

from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # MOD = 10 ** 9 + 7
        # n = len(s)
        # x_prefix = [0] * n
        # x_sum_prefix = [0] * n
        # current_x = 0
        # current_x_sum = 0
        # for i, digit in enumerate(s):
        #     if digit != '0':
        #         current_x = current_x * 10 + int(digit)
        #         current_x_sum += int(digit)
        #     x_prefix[i] = current_x
        #     x_sum_prefix[i] = current_x_sum
            
        # ans = [0] * len(queries)
        # for i, (l, r) in enumerate(queries):
        #     right_end = x_prefix[r]
        #     left_end = x_prefix[l - 1] if l > 0 else 0
        #     length = len(str(right_end)) - len(str(left_end))
        #     current_x = right_end - left_end * (10 ** (length))
        #     current_x_sum = x_sum_prefix[r] - (x_sum_prefix[l - 1] if l > 0 else 0)
        #     ans[i] = (current_x * current_x_sum) % MOD
            
        # return ans
        
        n = len(s)
        MOD = 10 ** 9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        prefix_val = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        prefix_cnt = [0] * (n + 1)
        
        current_val = current_sum = current_cnt = 0
        for i in range(n):
            if s[i] != '0':
                digit = int(s[i])
                current_val = (current_val * 10 + digit) % MOD
                current_sum += digit
                current_cnt += 1
                
            prefix_val[i + 1] = current_val
            prefix_sum[i + 1] = current_sum
            prefix_cnt[i + 1] = current_cnt
            
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            left_val = prefix_val[l]
            right_val = prefix_val[r + 1]
            
            left_sum = prefix_sum[l]
            right_sum = prefix_sum[r + 1]
            
            left_cnt = prefix_cnt[l]
            right_cnt = prefix_cnt[r + 1]
            
            count = (right_cnt - left_cnt)
            x = (right_val - left_val * pow10[count]) % MOD
            ans[i] = (x * (right_sum - left_sum)) % MOD
        
        return ans