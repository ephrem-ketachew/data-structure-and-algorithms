from collections import defaultdict
def countCompleteSubarrays(nums):
    count = defaultdict(int)
    left = 0
    uniqueElements = len(set(nums))
    uniqueInWindow = 0
    totalSubarrays = 0

    for right in range(len(nums)):
        if count[nums[right]] == 0:
            uniqueInWindow += 1
        count[nums[right]] += 1
    
        while uniqueElements == uniqueInWindow:
            totalSubarrays += len(nums) - right
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                uniqueInWindow -= 1
            left += 1

    return totalSubarrays


# def countCompleteSubarrays(nums):
#     uniqueElements = set(nums)
#     numberOfCompleteSubarrays = 0
#     for i in range(0, len(nums) - len(uniqueElements) + 1):
#         for j in range(i + len(uniqueElements) - 1, len(nums)):
#             subArray = nums[i:j + 1]
#             subArray = set(subArray)
#             if subArray == uniqueElements:
#                 numberOfCompleteSubarrays += len(nums) - j
#                 break

#     return numberOfCompleteSubarrays