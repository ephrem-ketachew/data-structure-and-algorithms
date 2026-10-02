class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # m, n = len(str1), len(str2)
        # dp = [[''] * (n + 1) for _ in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         if str1[i] == str2[j]:
        #             dp[i + 1][j + 1] = dp[i][j] + str1[i]
        #         else:
        #             if len(dp[i + 1][j]) >= len(dp[i][j + 1]):
        #                 dp[i + 1][j + 1] = dp[i + 1][j]
        #             else:
        #                 dp[i + 1][j + 1] = dp[i][j + 1]

        # common_seq = dp[m][n]
        # additions = []
        # curr = ''
        # i = j = 0
        # while i < len(common_seq) and j < m:
        #     if common_seq[i] == str1[j]:
        #         additions.append(curr)
        #         curr = ''
        #         i += 1
        #         j += 1
        #     else:
        #         curr += str1[j]
        #         j += 1

        # while j < m:
        #     curr += str1[j]
        #     j += 1

        # additions.append(curr)

        # ans = additions[0]
        # i = j = 0
        # while i < len(common_seq) and j < n:
        #     if common_seq[i] == str2[j]:
        #         ans += common_seq[i] + additions[i + 1]
        #         i += 1
        #         j += 1
        #     else:
        #         ans += str2[j]
        #         j += 1

        # while j < n:
        #     ans += str2[j]
        #     j += 1

        # return ans

        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        i, j = m, n
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1

        while i > 0:
            res.append(str1[i - 1])
            i -= 1

        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return ''.join(res[::-1])