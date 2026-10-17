class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def func(num):
            s = 0
            for d in str(num):
                s += int(d)
            return s

        sorted_nums = sorted(nums, key=lambda x: (func(x), x))
        pos = defaultdict(int)
        for i, num in enumerate(sorted_nums):
            pos[num] = i

        count = 0
        for i, num in enumerate(nums):
            target_idx = pos[num]
            while i != target_idx:
                count += 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                target_idx = pos[nums[i]]

        return count