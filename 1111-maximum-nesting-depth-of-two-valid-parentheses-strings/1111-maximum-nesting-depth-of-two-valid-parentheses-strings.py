class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        balance = 0
        for ch in seq:
            if ch == '(':
                balance += 1
                if balance % 2 == 1:
                    ans.append(0)
                else:
                    ans.append(1)
            else:
                balance -= 1
                if balance % 2 == 1:
                    ans.append(1)
                else:
                    ans.append(0)
                    
        return ans