# 3439. Reschedule Meetings for Maximum Free Time I
# Medium
# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

# The relative order of all the meetings should stay the same and they should remain non-overlapping.

# Return the maximum amount of free time possible after rearranging the meetings.

# Note that the meetings can not be rescheduled to a time outside the event.

# Example 1:

# Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]

# Output: 2

# Explanation:


# Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

# Example 2:

# Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]

# Output: 6

# Explanation:

# Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

# Example 3:

# Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

# Output: 0

# Explanation:

# There is no time during the event not occupied by meetings.

# Constraints:

# 1 <= eventTime <= 109
# n == startTime.length == endTime.length
# 2 <= n <= 105
# 1 <= k <= n
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0] - 0]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        
        max_free = win_free = sum(gaps[: k + 1])
        
        for i in range(k + 1, len(gaps)):
            win_free += gaps[i] - gaps[i - (k + 1)]
            max_free = max(max_free, win_free)
            
        return max_free
        
# solution = Solution()
# eventTime = 5
# k = 1
# startTime = [1,3]
# endTime = [2,5]

# eventTime = 10
# k = 1
# startTime = [0,2,9]
# endTime = [1,4,10]

# eventTime = 5
# k = 2
# startTime = [0,1,2,3,4]
# endTime = [1,2,3,4,5]
# print(solution.maxFreeTime(eventTime, k, startTime, endTime))