def summaryRanges(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [str(nums[0])]

    output = []
    minBoundary= nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            if minBoundary == nums[i - 1]:
                newElement = str(minBoundary)
                minBoundary = nums[i]
            else:
                newElement = str(minBoundary) + '->' + str(nums[i-1])
                minBoundary = nums[i]
            output.append(newElement)

    if minBoundary == nums[i]:
        newElement = str(minBoundary)
    else:
        newElement = str(minBoundary) + '->' + str(nums[i])
    output.append(newElement)

    return output