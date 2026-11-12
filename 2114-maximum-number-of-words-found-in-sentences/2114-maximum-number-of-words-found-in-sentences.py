class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)