class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        counter = Counter(chars)
        ans = 0
        for word in words:
            if Counter(word) <= counter:
                ans += len(word)
        return ans