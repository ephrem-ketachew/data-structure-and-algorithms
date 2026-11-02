class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter = Counter((s1 + ' ' + s2).split())
        return [word for word, freq in counter.items() if freq == 1]