def removeElement(nums, val):
    while nums.count(val) > 0:
        nums.remove(val)
    return len(nums)