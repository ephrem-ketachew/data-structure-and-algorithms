class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        curr = prev = 0
        last = ''
        for ch in s:
            if ch == last:
                if prev > 0:
                    count += 1
                    prev -= 1
                curr += 1
            else:
                if last != '':
                    count += 1
                    curr -= 1
                prev = curr
                curr = 1
            last = ch

        return count
