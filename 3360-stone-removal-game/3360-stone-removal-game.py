class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        while n > 0:
            if n < remove:
                return False
            n -= remove
            remove -= 1
            if n < remove:
                return True
            n -= remove
            remove -= 1
        
        return False
