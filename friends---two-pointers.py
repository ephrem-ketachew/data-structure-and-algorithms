# 825. Friends Of Appropriate Ages
# Medium
# There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

# A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.

# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

# Return the total number of friend requests made.

# Example 1:

# Input: ages = [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:

# Input: ages = [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:

# Input: ages = [20,30,100,110,120]
# Output: 3
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

# Constraints:

# n == ages.length
# 1 <= n <= 2 * 104
# 1 <= ages[i] <= 120

from typing import List
import bisect

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # ages.sort()
        
        # count = 0
        # for age in ages:
        #     lower_bound = bisect.bisect_right(ages, 0.5 * age + 7)
        #     upper_bound = bisect.bisect_right(ages, age) - 2
            
        #     if upper_bound >= lower_bound:
        #         count += upper_bound - lower_bound + 1
                
        # return count
        
        # ages.sort()
        
        # left = 0
        # count = 0
        # dup = 0
        # for right, age in enumerate(ages):
        #     lower_bound = 0.5 * age + 7
            
        #     while left < len(ages) and ages[left] <= lower_bound:
        #         left += 1
                
        #     if left <= right - 1:
        #         count += right - left
                
        #     if right > 0 and ages[right] == ages[right - 1]:
        #         dup += 1
        #     else:
        #         dup = 0
        #     if age > 14:
        #         count += dup
                
        # return count
        
        freq = [0] * 121
        
        for age in ages:
            freq[age] += 1
            
        count = 0
        for a in range(1, 121):
            if freq[a] == 0:
                continue
            lower = int(0.5 * a + 7)
            for b in range(lower + 1, a + 1):
                count += freq[a] * freq[b]
                if a == b:
                    count -= freq[a]
                        
        return count
                
    
    
# solution = Solution()
# ages = [101,56,69,48,30]
# print(solution.numFriendRequests(ages))