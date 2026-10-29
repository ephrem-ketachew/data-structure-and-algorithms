class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        dp = {1:0}
        for num in range(lo, hi + 1):
            curr = num
            stack = []
            cnt = 0
            while curr > 1:
                stack.append(curr)
                if curr in dp:
                    cnt = dp[curr]
                    break
                if curr % 2 == 0:
                    curr //= 2
                else:
                    curr = curr * 3 + 1

            while stack:
                curr = stack.pop()
                dp[curr] = cnt
                cnt += 1
            
            power.append((num, dp[num]))

        power.sort(key=lambda x: (x[1], x[0]))
        return power[k - 1][0]

        
