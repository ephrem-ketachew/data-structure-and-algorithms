class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        max_depth = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                open -= 1
            max_depth = max(max_depth, open)

        return max_depth