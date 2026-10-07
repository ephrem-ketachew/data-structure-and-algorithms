class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        removal_count = 0
        open = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                if open == 0:
                    removal_count += 1
                else:
                    open -= 1

        removal_count += open

        ans = set()
        def is_valid(arr: list[str]) -> bool:
            open = 0
            for ch in arr:
                if ch == '(':
                    open += 1
                elif ch == ')':
                    open -= 1
                if open < 0:
                    return False
            return open == 0

        def backtrack(start: int, arr: list[str], n: int) -> None:
            if len(arr) == n:
                if is_valid(arr):
                    ans.add(''.join(arr))
                return

            if start == len(s) or len(arr) + len(s) - start < n:
                return

            for i in range(start, len(s)):
                arr.append(s[i])
                backtrack(i + 1, arr[:], n)
                if s[i] == '(' or s[i] == ')':
                    arr.pop()

        backtrack(0, [], len(s) - removal_count)
        return list(ans) if ans else [""]