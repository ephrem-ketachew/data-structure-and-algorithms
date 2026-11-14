class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        l_win_sum = sum(nums[:l])
        if l_win_sum > 0:
            min_sum = l_win_sum
            
        for i in range(l, len(nums)):
            l_win_sum += nums[i]
            l_win_sum -= nums[i - l]
            
            if l_win_sum > 0:
                min_sum = min(min_sum, l_win_sum)
            
            win_sum = l_win_sum
            for j in range(i - l, max(i - r, -1), -1):
                win_sum += nums[j]
                if win_sum > 0:
                    min_sum = min(min_sum, win_sum)
                
            if min_sum == 1:
                return 1
            
        return min_sum if min_sum != float('inf') else -1