class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)

        def rotate_sortable(arr: list[int]) -> bool:
            if len(set(arr)) == 1:
                return True 

            n = len(arr)
            pivot_idx = arr.index(max(arr))
            skip = 0
            while arr[pivot_idx] == arr[(pivot_idx + 1) % n]:
                pivot_idx = (pivot_idx + 1) % n
                skip += 1

            for i in range(pivot_idx + 1, pivot_idx + n - skip):
                cur = arr[i % n]
                nxt = arr[(i + 1) % n]
                if cur > nxt:
                    return False
            return True

        def is_sortable(k: int) -> bool:
            global_min, global_max = float('inf'), float('-inf')
            i = 0
            while i < n:
                arr = nums[i:i+k]
                if not rotate_sortable(arr):
                    return False

                local_min = min(arr)
                local_max = max(arr)
                if local_min < global_max:
                    return False

                global_max = max(global_max, local_max)
                global_min = min(global_min, local_min)

                i += k

            return True

        total = 0
        for k in divisors:
            if is_sortable(k):
                total += k

        return total
