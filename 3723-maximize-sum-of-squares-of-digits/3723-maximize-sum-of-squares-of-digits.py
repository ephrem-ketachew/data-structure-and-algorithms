class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum:
            return ''

        ans = []
        while sum > 0:
            curr = min(sum, 9)
            ans.append(str(curr))
            sum -= curr

        ans.extend(['0'] * (num - len(ans)))
        return ''.join(ans)