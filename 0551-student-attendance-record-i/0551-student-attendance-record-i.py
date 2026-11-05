class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False

        count = 0
        for ch in s:
            if ch == 'L':
                count += 1
            else:
                count = 0
            if count == 3:
                return False

        return True