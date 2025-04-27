def max_subarray_length(nums, k):
    max_length = 0
    window_sum = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum >= k:
            window_sum -= nums[left]
            left += 1
            
        max_length = max(max_length, right - left + 1)
                
    return max_length
            