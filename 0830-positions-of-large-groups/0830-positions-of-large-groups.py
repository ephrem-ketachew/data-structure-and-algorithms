class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        ans = []
        prev = 'A'
        count = 0
        start_idx = -1
        s += 'A'
        for i, char in enumerate(s):
            if char == prev:
                count += 1
            else:
                if count >= 3:
                    ans.append([start_idx, i - 1])
                count = 1
                start_idx = i
                prev = char

        return ans
