class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x:len(x))
        ans = []
        for i, word in enumerate(words):
            for j, s in enumerate(words):
                if i != j and word in s:
                    ans.append(word)
                    break

        return ans