# 3440. Reschedule Meetings for Maximum Free Time II
# Medium
# Topics
# You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

# These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

# You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

# Return the maximum amount of free time possible after rearranging the meetings.

# Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

# Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.


# Example 1:

# Input: eventTime = 5, startTime = [1,3], endTime = [2,5]

# Output: 2

# Explanation:

# Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

# Example 2:

# Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

# Output: 7

# Explanation:



# Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].

# Example 3:

# Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

# Output: 6

# Explanation:

# Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].

# Example 4:

# Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

# Output: 0

# Explanation:

# There is no time during the event not occupied by meetings. 

# Constraints:

# 1 <= eventTime <= 109
# n == startTime.length == endTime.length
# 2 <= n <= 105
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # gaps = [startTime[0]]
        # for i in range(1, len(startTime)):
        #     gaps.append(startTime[i] - endTime[i - 1])
        # gaps.append(eventTime - endTime[-1])
        
        # event_duration = []
        # for i in range(len(startTime)):
        #     event_duration.append(endTime[i] - startTime[i])
            
        # max_gap = 0
        # for i in range(len(gaps) - 1):
        #     gap = gaps[i] + gaps[i + 1]
        #     found = False
        #     for k in range(i):
        #         if gaps[k] >= event_duration[i]:
        #             gap += event_duration[i]
        #             found = True
        #             break
        #     if not found:
        #         for k in range(i + 2, len(gaps)):
        #             if gaps[k] >= event_duration[i]:
        #                 gap += event_duration[i]
        #                 break
        #     max_gap = max(max_gap, gap)
            
        # return max_gap
        
        n = len(startTime)
        na_space_avail = [False] * n        # non adjacent space available at index i?   
        t1, t2 = 0, 0     #maximum non adjacent free spaces available so far in both directions
        
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                na_space_avail[i] = True
                
            t1 = max(
                t1,
                startTime[i] - (endTime[i - 1] if i > 0 else 0)
            )
            
            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                na_space_avail[n - i - 1] = True
                
            t2 = max(
                t2,
                (startTime[n - i] if i > 0 else eventTime) - endTime[n - i - 1]
            )
            
        max_gap = 0
        for i in range(n):
            left = endTime[i - 1] if i > 0 else 0
            right = startTime[i + 1] if i + 1 < n else eventTime
            if na_space_avail[i]:
                max_gap = max(max_gap, right - left)
            else:
                max_gap = max(max_gap, right - left - (endTime[i] - startTime[i]))
                
        return max_gap
    
# solution = Solution()
# eventTime = 5
# startTime = [1,3]
# endTime = [2,5]
# eventTime = 10
# startTime = [0,7,9]
# endTime = [1,8,10]
# eventTime = 10
# startTime = [0,3,7,9]
# endTime = [1,4,8,10]
# eventTime = 5
# startTime = [0,1,2,3,4]
# endTime = [1,2,3,4,5]
# print(solution.maxFreeTime(eventTime, startTime, endTime))