class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        for num in range(lo, hi + 1):
            cnt = 0
            x = num
            while x > 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = x * 3 + 1
                cnt += 1
            power.append((num, cnt))

        power.sort(key=lambda x: (x[1], x[0]))
        
        return power[k - 1][0]

        