class Solution:
    def freqAlphabets(self, s: str) -> str:
        arr = []
        i, n = 0, len(s)
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                num = int(s[i:i+2])
                arr.append(chr(96 + num))
                i += 3
            else:
                arr.append(chr(96 + int(s[i])))
                i += 1

        return ''.join(arr)
