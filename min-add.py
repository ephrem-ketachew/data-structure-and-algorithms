# 921. Minimum Add to Make Parentheses Valid
# Medium
# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3
 

# Constraints:

# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = []
        # count_insert = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append('(')
        #     else:
        #         if stack:
        #             stack.pop()
        #         else:
        #             count_insert += 1
        
        # count_insert += len(stack)
        
        # return count_insert
        
        balance = 0
        count_insert = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    count_insert += 1
        
        count_insert += balance
        
        return count_insert