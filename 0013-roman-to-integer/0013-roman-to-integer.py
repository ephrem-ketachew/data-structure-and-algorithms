class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        specials = {'I': 'VX', 'X': 'LC', 'C': 'DM'}
        num = i = 0
        n = len(s)
        while i < n:
            if i + 1 < n and s[i] in specials and s[i + 1] in specials[s[i]]:
                num += map[s[i + 1]] - map[s[i]]
                i += 2
            else:
                num += map[s[i]]
                i += 1

        return num