class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter1, counter2 = Counter(s1.split()), Counter(s2.split())
        ans = []
        for word in counter1:
            if counter1[word] == 1 and word not in counter2:
                ans.append(word)

        for word in counter2:
            if counter2[word] == 1 and word not in counter1:
                ans.append(word)

        return ans