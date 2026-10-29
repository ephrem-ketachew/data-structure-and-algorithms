class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        sum1 = [0] * (n * 4)
        sum2 = [0] * (n * 4)
        lazy = [0] * (n * 4)

        def apply(node, start, end, val):
            length = end - start + 1
            sum2[node] = (sum2[node] + 2 * val * sum1[node] + val * val * length) % MOD
            sum1[node] = (sum1[node] + val * length) % MOD
            lazy[node] += val

        def push_down(node, start, end):
            if lazy[node] != 0:
                mid = (start + end) // 2
                apply(2 * node, start, mid, lazy[node])
                apply(2 * node + 1, mid + 1, end, lazy[node])
                lazy[node] = 0

        def push_up(node):
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD

        def update(node, start, end, l, r, val):
            if r < start or l > end:
                return

            if l <= start and end <= r:
                apply(node, start, end, val)
                return

            push_down(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            push_up(node)

        total = 0
        last_seen = {}
        for j in range(n):
            val = nums[j]
            start_idx = last_seen.get(val, -1) + 1
            update(1, 0, n - 1, start_idx, j, 1)
            total = (total + sum2[1]) % MOD
            last_seen[val] = j

        return total