class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        dp = {1:0}
        for num in range(lo, hi + 1):
            x = num
            stack = []
            cnt = 0
            while x > 1:
                stack.append(x)
                if x in dp:
                    cnt = dp[x]
                    break
                if x % 2 == 0:
                    x //= 2
                else:
                    x = x * 3 + 1

            while stack:
                x = stack.pop()
                dp[x] = cnt
                cnt += 1
            
            power.append((num, dp[num]))

        print(dp)
        power.sort(key=lambda x: (x[1], x[0]))
        return power[k - 1][0]

        
