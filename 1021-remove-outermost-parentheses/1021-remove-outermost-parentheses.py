class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        cur = []
        open = close = 0
        for ch in s:
            if ch == '(':
                open += 1
            else:
                close += 1
            
            cur.append(ch)
            
            if open == close:
                ans.append(''.join(cur[1:-1]))
                cur = []
                open = close = 0
                
        return ''.join(ans)