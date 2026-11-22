class Solution:
    def checkString(self, s: str) -> bool:
        a_last_idx = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a':
                a_last_idx = i
                break

        if a_last_idx == -1:
            return True

        b_first_idx = s.find('b')
        if b_first_idx == -1:
            return True

        return a_last_idx < b_first_idx