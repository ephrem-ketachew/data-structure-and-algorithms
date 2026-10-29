class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                buffer = []
                while stack[-1] != '(':
                    buffer.append(stack.pop())
                stack.pop()
                stack += buffer
            else:
                stack.append(ch)
                
        return ''.join(stack)