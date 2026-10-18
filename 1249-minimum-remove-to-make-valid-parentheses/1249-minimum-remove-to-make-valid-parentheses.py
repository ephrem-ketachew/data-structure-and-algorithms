class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()

        while stack:
            remove.add(stack.pop())

        ans = []
        for i, ch in enumerate(s):
            if i not in remove:
                ans.append(ch)

        return ''.join(ans)