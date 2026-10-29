class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for ch in s:
            if ch.isdecimal():
                nums.add(int(ch))

        nums = list(nums)
        nums.sort(reverse=True)
        if len(nums) > 1:
            return nums[1]
        
        return -1