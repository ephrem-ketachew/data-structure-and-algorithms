class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        sorted_s = ''.join(sorted(s))
        if s == sorted_s:
            return 0

        if len(s) == 2:
            return -1

        if s[0] == sorted_s[0] or s[-1] == sorted_s[-1]:
            return 1

        if s[0] == sorted_s[-1] and s[-1] == sorted_s[0]:
            if s.count(sorted_s[0]) > 1 or s.count(sorted_s[-1]) > 1:
                return 2
            return 3

        return 2

        
        