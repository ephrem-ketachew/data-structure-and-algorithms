# 986. Interval List Intersections
# Medium
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# Example 1:


# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Example 2:

# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []

# Constraints:

# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 109
# endi < starti+1
# 0 <= startj < endj <= 109 
# endj < startj+1

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        # i = 0
        # for (start, end) in firstList:
        #     while i < len(secondList) and secondList[i][0] <= end:
        #         first, second = secondList[i]
        #         left = max(start, first)
        #         right = min(end, second)
        #         if left <= right:
        #             if intersection and intersection[-1][-1] == left:
        #                 intersection[-1][-1] = right
        #             else:
        #                 intersection.append([left, right])          
        #         i += 1
            
        #     if i > 0:    
        #         i -= 1
                
        # return intersection
        
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            start = max(first_start, second_start)
            end = min(first_end, second_end)
            
            if start <= end:
                intersection.append([start, end])
                
            if first_end <= second_end:
                i += 1
            else:
                j += 1
                
        return intersection
    
solution = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
firstList = [[1,3],[5,9]]
secondList = []
print(solution.intervalIntersection(firstList, secondList))