# 394. Decode String
# Medium

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # digit = []
        # for ch in s:
        #     if ch == ']':
        #         cur_s = []
        #         while stack[-1] != '[':
        #             cur_s.append(stack.pop())
        #         stack.pop()
                
        #         cur_s.reverse()
        #         cur_s = ''.join(cur_s)
        #         freq = stack.pop()
        #         stack.append(freq * cur_s)
        #     elif ch.isdecimal():
        #         digit.append(ch)
        #     elif ch == '[':
        #         if digit:
        #             num = int(''.join(digit))
        #             digit = []
        #             stack.extend([num, '['])
        #     else:
        #         stack.append(ch)
                    
        # return ''.join(stack)
        
        digit = []
        cur_str = []
        i = 0
        ans = ''
        while i < len(s):
            if s[i].isdecimal():
                while s[i].isdecimal():
                    digit.append(s[i])
                    i += 1
                
                num = int(''.join(digit))
                digit = []
            
                i += 1
                cur_str = []
                open = 1
                while open > 0:
                    if s[i] == ']':
                        open -= 1
                        if open == 0:
                            break
                    if s[i] == '[':
                        open += 1
                    cur_str.append(s[i])
                    i += 1
                    
                cur_s = ''.join(cur_str)
                cur_str = []
                
                ans += num * self.decodeString(cur_s)
                
                i += 1
            else:
                while i < len(s) and s[i].isalpha():
                    cur_str.append(s[i])
                    i += 1
                    
                cur_s = ''.join(cur_str)
                cur_str = []
                ans += cur_s
            
        return ans