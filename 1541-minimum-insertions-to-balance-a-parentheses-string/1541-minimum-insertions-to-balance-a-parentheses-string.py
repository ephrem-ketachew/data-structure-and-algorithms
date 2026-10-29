class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        insertion = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                open += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    if open > 0:
                        open -= 1
                    else:
                        insertion += 1
                    i += 2
                else:
                    if open > 0:
                        open -= 1
                        insertion += 1
                    else:
                        insertion += 2
                    i += 1
        insertion += open * 2
        return insertion
