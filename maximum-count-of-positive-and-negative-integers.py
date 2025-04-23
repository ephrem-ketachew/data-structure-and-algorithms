def maximumCount(nums):
    pos = 0
    neg = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            neg += 1
        elif nums[i] > 0:
            pos += 1
    return max(neg, pos)