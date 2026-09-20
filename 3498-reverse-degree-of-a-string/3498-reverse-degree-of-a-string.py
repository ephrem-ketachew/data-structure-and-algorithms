class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(ch) - 97)) * i for i, ch in enumerate(s, start=1))