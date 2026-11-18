class Solution:
    def minChanges(self, s: str) -> int:
        # even_divisors = []
        # n = len(s)
        # for i in range(2, n + 1):
        #     if n % i == 0 and i % 2 == 0:
        #         even_divisors.append(i)

        # min_flips = n
        # for num in even_divisors:
        #     count_ones = 0
        #     flips = 0
        #     for i in range(n):
        #         if s[i] == '1':
        #             count_ones += 1
        #         if (i + 1) % num == 0:
        #             flips += min(count_ones, num - count_ones)
        #             count_ones = 0

        #     min_flips = min(min_flips, flips)

        # return min_flips
        
        flips = 0
        count_ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_ones += 1
            if (i + 1) % 2 == 0:
                flips += min(count_ones, 2 - count_ones)
                count_ones = 0

        return flips