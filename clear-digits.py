# 3174. Clear Digits

# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

# Example 1:

# Input: s = "abc"

# Output: "abc"

# Explanation:

# There is no digit in the string.

# Example 2:

# Input: s = "cb34"

# Output: ""

# Explanation:

# First, we apply the operation on s[2], and s becomes "c4".

# Then we apply the operation on s[1], and s becomes "".

# Constraints:

# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit() and stack:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    
    
        # while True:
        #     for i in range(1, len(s)):
        #         if s[i].isdigit():
        #             s = s[:i - 1] + s[i + 1:]
        #             break
        #     else:
        #         break
        # return s
        
        
        
        # def __clear(s):
        #     my_string = ''
        #     stack = []
        #     for i in range(len(s)):
        #         if s[i].isdigit():
        #             if stack:
        #                 stack.pop()
        #                 while stack:
        #                     my_string = stack.pop() + my_string
        #                 my_string = my_string + s[i + 1:]
        #                 return my_string
        #         else:
        #             stack.append(s[i])
        #     return None
        # new_s = s
        # cleared_s = __clear(s)
        # while cleared_s is not None:
        #     new_s = cleared_s
        #     cleared_s = __clear(cleared_s)
            
        # return new_s
        
        
        
        # found = True
        # while found:
        #     found = False
        #     for i in range(len(s) -1, -1, -1):
        #         if s[i].isdigit():
        #             print(s[i])
        #             for j in range(i - 1, -1, -1):
        #                 if not s[j].isdigit():
        #                     found = True
        #                     s = s[0:j] + s[j + 1: i] + s[i +1:]
        #                     break
        #         if found:
        #             break
        # return s