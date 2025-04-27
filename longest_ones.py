def longest_ones(nums, k: int) -> int:
    left = 0
    max_ones = 0
    zeros = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
            
        max_ones = max(max_ones, right - left + 1)
        
    return max_ones



# def longest_ones(nums, k: int) -> int:
#     left = 0
#     max_ones = 0
#     sliding_window = []
    
#     for right in range(len(nums)):
#         sliding_window.append(nums[right])
#         while sliding_window.count(0) > k:
#             sliding_window.pop(0)
#             left += 1
#         max_ones = max(max_ones, right - left + 1)
        
#     return max_ones

print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))