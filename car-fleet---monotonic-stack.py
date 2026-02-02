# 853. Car Fleet
# Medium

# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

# You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

# A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

# Return the number of car fleets that will arrive at the destination.

# Example 1:

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

# Output: 3

# Explanation:

# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Example 2:

# Input: target = 10, position = [3], speed = [3]

# Output: 1

# Explanation:

# There is only one car, hence there is only one fleet.
# Example 3:

# Input: target = 100, position = [0,2,4], speed = [4,2,1]

# Output: 1

# Explanation:

# The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
# Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

# Constraints:

# n == position.length == speed.length
# 1 <= n <= 105
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # THE FIRST 1:39 HOURS WASTED SIMULATING😭😭😭😭😭
        
        # pos_spd = [[pos, spd] for pos, spd in zip(position, speed)]
        # pos_spd.sort()
        
        # stack = []
        # for i in range(len(pos_spd) - 1, -1, -1):
        #     cur_pos, cur_spd = pos_spd[i]
        #     while stack and cur_spd > stack[-1][1]:
        #         prev_pos, prev_spd = stack.pop()
        #         time_to_collide = (prev_pos - cur_pos) / (cur_spd - prev_spd)
        #         pos_to_collide = cur_pos + cur_spd * time_to_collide
        #         if pos_to_collide <= target:
        #             cur_spd = prev_spd
        #             cur_pos = pos_to_collide
        #         else:
        #             stack.append([prev_pos, prev_spd])
        #             break
        #     stack.append([cur_pos, cur_spd])
                       
        # print(pos_spd)
        # print(stack)
        # return len(stack)  
    
    
        # pos_spd = [[pos, spd] for pos, spd in zip(position, speed)]
        # pos_spd.sort()
        
        # stack = []
        # for i in range(len(pos_spd) - 1, -1, -1):
        #     cur_pos, cur_spd = pos_spd[i]
        #     cur_time = 0
        #     while stack and cur_spd > stack[-1][1]:
        #         prev_pos, prev_spd, time_travelled = stack.pop()
        #         time_to_collide = (prev_pos - (cur_pos + cur_spd * time_travelled)) / (cur_spd - prev_spd)
        #         pos_to_collide = cur_pos + cur_spd * time_to_collide
        #         if pos_to_collide <= target:
        #             cur_spd = prev_spd
        #             cur_pos = pos_to_collide
        #             cur_time = time_travelled + time_to_collide
        #         else:
        #             stack.append([prev_pos, prev_spd])
        #             break
        #     stack.append([cur_pos, cur_spd])
                       
        # return len(stack)   
        
        # NOW I GAVE UP AND SAW THE SOLUTION AND CODED IT
        
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
                
        return len(stack)
            
# solution = Solution()
# target = 12
# position = [10,8,0,5,3]
# speed = [2,4,1,1,3]
# print(solution.carFleet(target, position, speed))     