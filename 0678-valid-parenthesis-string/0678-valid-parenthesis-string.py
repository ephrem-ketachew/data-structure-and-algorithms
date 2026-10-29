class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open = 0
        # max_open = 0
        # for ch in s:
        #     if ch == '(':
        #         min_open += 1
        #         max_open += 1
        #     elif ch == ')':
        #         min_open -= 1
        #         max_open -= 1
        #     else:
        #         max_open += 1
        #         min_open -= 1
        #     if max_open < 0:
        #         return False

        #     if min_open < 0:
        #         min_open = 0

        # return min_open == 0

        memo = {}
        n = len(s)
        def dfs(i: int, open_count: int) -> bool:
            if open_count < 0:
                return False

            if i == n:
                return open_count == 0

            if (i, open_count) in memo:
                return memo[(i, open_count)]

            if s[i] == '(':
                res = dfs(i + 1, open_count + 1)
            elif s[i] == ')':
                res = dfs(i + 1, open_count - 1)
            else:
                res = dfs(i + 1, open_count + 1) or dfs(i + 1, open_count - 1) or dfs(i + 1, open_count)

            memo[(i, open_count)] = res
            return res

        return dfs(0, 0)