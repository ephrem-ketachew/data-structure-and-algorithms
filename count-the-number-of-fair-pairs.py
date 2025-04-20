def countFairPairs(nums, lower, upper):
    count = 0
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if(sum >= lower and sum <= upper):
                count += 1
    return count