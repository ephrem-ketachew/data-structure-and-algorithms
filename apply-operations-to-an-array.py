def applyOperations(nums):
    for i in range(len(nums) -1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    print(nums)
    for i in range(len(nums) -1):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if  nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
            else:
                break
    return nums