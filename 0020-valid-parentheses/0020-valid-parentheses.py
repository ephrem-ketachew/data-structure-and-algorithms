class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"{":"}", "(":")", "[":"]"}
        stack = []
        for ch in s:
            if ch in pair:
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                key = stack.pop()
                if pair[key] != ch:
                    return False
                
        return len(stack) == 0