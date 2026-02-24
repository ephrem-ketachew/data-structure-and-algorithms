# 224. Basic Calculator
# Hard

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 
# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        # stack = []
        # digit = []
        # for i, ch in enumerate(s):
        #     if ch == ' ':
        #         continue
        #     if ch in ['(', '+', '-']:
        #         stack.append(ch)
                
        #     elif ch.isdecimal():
        #         digit.append(ch)
                
        #         if i + 1 == len(s) or (not s[i + 1].isdecimal()):
        #             num = ''.join(digit)
        #             if stack and stack[-1] == '-':
        #                 if len(stack) == 1 or stack[-2] == '(':
        #                     stack.pop()
        #                     num = '-' + num
                            
        #             stack.append(int(num))
                    
        #             digit = []
                    
        #     elif ch == ')':
        #         buffer = []
        #         while stack[-1] != '(':
        #             buffer.append(stack.pop())
                    
        #         stack.pop()
        #         score = int(buffer.pop())
        #         while buffer:
        #             op = buffer.pop()
        #             b = buffer.pop()
                    
        #             if op == '+':
        #                 score += b
        #             elif op == '-':
        #                 score -= b
                    
        #         if stack and stack[-1] == '-':
        #             if len(stack) == 1 or stack[-2] == '(':
        #                 stack.pop()
        #                 score *= -1
                    
        #         if score < 0:
        #             if stack:
        #                 op = stack.pop()
        #                 if op == '+':
        #                     stack.append('-')
        #                     stack.append(abs(score))
        #                 elif op == '-':
        #                     stack.append('+')
        #                     stack.append(abs(score))
        #             else:
        #                 stack.append(score)
        #         else:
        #             stack.append(score)
                    
        # buffer = []
        # while stack:
        #     buffer.append(stack.pop())
            
        # score = int(buffer.pop())
        # while buffer:
        #     op = buffer.pop()
        #     b = buffer.pop()
            
        #     if op == '+':
        #         score += b
        #     elif op == '-':
        #         score -= b
            
        # return score
        
        stack = []
        digit = []
        for i, ch in enumerate(s):
            if ch == ' ':
                continue
            if ch in ['(', '+', '-']:
                stack.append(ch)
                
            elif ch.isdecimal():
                digit.append(ch)
                if i + 1 == len(s) or not (s[i + 1].isdecimal()):
                    stack.append(int(''.join(digit)))
                    digit = []
                    
            elif ch == ')':
                buffer = []
                while stack[-1] != '(':
                    buffer.append(stack.pop())
                    
                score = buffer.pop()
                if score == '-':
                    score = -1 * buffer.pop()
                    
                while buffer:
                    op = buffer.pop()
                    num = buffer.pop()
                    
                    if op == '+':
                        score += num
                    elif op == '-':
                        score -= num
                        
                stack.pop()
                stack.append(score)
                
                
        buffer = []
        while stack:
            buffer.append(stack.pop())
            
        score = buffer.pop()
        if score == '-':
            score = -1 * buffer.pop()
            
        while buffer:
            op = buffer.pop()
            num = buffer.pop()
            
            if op == '+':
                score += num
            elif op == '-':
                score -= num
                
        return score