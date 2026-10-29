class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(opn: int, cls: int, curr: List[str]) -> None:
            if opn == 0 and cls == 0:
                ans.append(''.join(curr[:]))
                return
            
            if opn > 0:
                curr.append('(')
                backtrack(opn - 1, cls + 1, curr)
                curr.pop()
                
            if cls > 0:
                curr.append(')')
                backtrack(opn, cls - 1, curr)
                curr.pop()
                
        backtrack(n, 0, [])
        return ans