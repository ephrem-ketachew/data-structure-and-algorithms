class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pdt = 1
        sum = 0
        for d in str(n):
            pdt *= int(d)
            sum += int(d)

        return pdt - sum