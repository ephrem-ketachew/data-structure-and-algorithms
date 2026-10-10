class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        diff_arr = [abs(nums1[i] - nums2[i]) for i in range(n)]
        if sum(diff_arr) <= k:
            return 0

        counter = Counter(diff_arr)
        heap = []
        for num in counter:
            heapq.heappush(heap, -num)

        while k > 0:
            num = -heapq.heappop(heap)
            freq = counter[num]
            if freq <= 0:
                continue
            counter[num] -= k
            if freq - k > 0:
                heapq.heappush(heap, -num)
                heapq.heappush(heap, -(num - 1))
                counter[num - 1] += k
            else:
                heapq.heappush(heap, -(num - 1))
                counter[num - 1] += freq

            k -= freq

        return sum(counter[num] * (num * num) for num in counter if counter[num] > 0)
