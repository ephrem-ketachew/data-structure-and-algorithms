class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        # n = len(nums) - 1
        # max_bits = n.bit_length()
        # duplicate = 0
        # for b in range(max_bits):
        #     mask = 1 << b
        #     count_bits = 0
        #     for num in nums:
        #         if mask & num:
        #             count_bits += 1

        #     count_base = 0
        #     for i in range(1, n + 1):
        #         if mask & i:
        #             count_base += 1

        #     if count_bits > count_base:
        #         duplicate |= mask

        # return duplicate

        # n = len(nums)
        # mask = 1 << (n + 1)
        # for num in nums:
        #     if mask & (1 << num):
        #         return num
        #     mask |= 1 << num

        # return 'from dust i came, to dust i shall return'