class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # max_len = 0
        # n = len(s)
        # for i, ch in enumerate(s):
        #     if ch == '(':
        #         open = 1
        #         for j in range(i + 1, n):
        #             if s[j] == '(':
        #                 open += 1
        #             else:
        #                 open -= 1
        #             if open < 0:
        #                 break
        #             if open == 0:
        #                 k = j - i + 1
        #                 max_len = max(max_len, k)

        # return max_len

        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len