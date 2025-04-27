def max_subarray_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum


# def max_subarray_sum(nums, k):
#     max_sum = float('-inf')
#     left = 0
#     for right in range(k, len(nums)):
#         window_sum = sum(nums[left: right])
#         if window_sum > max_sum:
#             max_sum = window_sum
#         left += 1
#     return max_sum