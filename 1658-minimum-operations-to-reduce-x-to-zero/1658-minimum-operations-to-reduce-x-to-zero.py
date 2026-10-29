class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        summ = sum(nums)

        if summ < x:
            return -1
            
        target = summ - x
        win_sum, left, max_len = 0, 0, -1
        
        for right in range(len(nums)):
            win_sum += nums[right]
            while win_sum > target:
                win_sum -= nums[left]
                left += 1
            
            if win_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1