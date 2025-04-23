def divideArray(nums):
    pairs = {}
    for num in nums:
        if num in pairs and pairs[num] is None:
            pairs[num] = num
        else:
            pairs[num] = None

    return not None in pairs.values()