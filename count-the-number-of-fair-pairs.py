# Definition for singly-linked list.
import bisect as b 

def countFairPairs(nums,lower,upper):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        lowestBound = lower - nums[i]
        upperBound = upper - nums[i]
        left = b.bisect_left(nums,lowestBound, i+1)
        right = b.bisect_right(nums, upperBound, i + 1)
        count += (right - left)
    return count