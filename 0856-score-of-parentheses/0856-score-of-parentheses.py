class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                val = 1 if val == 0 else 2 * val
                stack[-1] += val
                
        return stack[0]