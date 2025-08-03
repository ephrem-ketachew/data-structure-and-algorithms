# 2332. The Latest Time to Catch a Bus
# Medium
# You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.

# You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.

# When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.

# More formally when a bus arrives, either:

# If capacity or fewer passengers are waiting for a bus, they will all get on the bus, or
# The capacity passengers with the earliest arrival times will get on the bus.
# Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.

# Note: The arrays buses and passengers are not necessarily sorted.

# Example 1:

# Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
# Output: 16
# Explanation: Suppose you arrive at time 16.
# At time 10, the first bus departs with the 0th passenger. 
# At time 20, the second bus departs with you and the 1st passenger.
# Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1st passenger to catch the bus.
# Example 2:

# Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
# Output: 20
# Explanation: Suppose you arrive at time 20.
# At time 10, the first bus departs with the 3rd passenger. 
# At time 20, the second bus departs with the 5th and 1st passengers.
# At time 30, the third bus departs with the 0th passenger and you.
# Notice if you had arrived any later, then the 6th passenger would have taken your seat on the third bus.
 
# Constraints:

# n == buses.length
# m == passengers.length
# 1 <= n, m, capacity <= 105
# 2 <= buses[i], passengers[i] <= 109
# Each element in buses is unique.
# Each element in passengers is unique.

from typing import List
from collections import Counter

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # buses.sort()
        # passengers.sort()

        # j = i = 0
        # count_passenger = 0
        # volume = [0] * len(buses)
        # while i < len(passengers) and j < len(buses):
        #     if passengers[i] <= buses[j] and count_passenger < capacity:
        #         count_passenger += 1
        #         volume[j] += 1
        #         i += 1
        #     else:
        #         j += 1
        #         count_passenger = 0
        
        # passengers_hash = Counter(passengers)
        # start = passengers[i - 1]
        # if volume[-1] < capacity:
        #     start = buses[-1]
        # for k in range(start, -1, -1):
        #     if k not in passengers_hash:
        #         return k
            
            
        # better approach
        buses.sort()
        passengers.sort()
        
        passengers_on_last_bus = 0
        pas_idx = 0
        for bus in buses:
            passengers_on_board = 0
            while pas_idx < len(passengers) and passengers[pas_idx] <= bus and passengers_on_board < capacity:
                passengers_on_board += 1
                pas_idx += 1
            passengers_on_last_bus = passengers_on_board
            
        if passengers_on_last_bus < capacity:
            start = buses[-1]
        else:
            start = passengers[pas_idx - 1]
            
        passengers = set(passengers)
        for arrival_time in range(start, -1, -1):
            if arrival_time not in passengers:
                return arrival_time
            
            
# solution = Solution()
# buses = [10,20]
# passengers = [2,17,18,19]
# capacity = 2
# buses = [20,30,10]
# passengers = [19,13,26,4,25,11,21]
# capacity = 2
# buses = [3]
# passengers = [2,4]
# capacity = 2
# buses = [2,3]
# passengers = [4,2]
# capacity = 1
# buses = [3]
# passengers = [2]
# capacity = 1
# buses = [3,4]
# passengers = [2,4]
# capacity = 1
# buses = [6,8,18,17]
# passengers = [6,8,17]
# capacity = 1
# buses = [18,8,3,12,9,2,7,13,20,5]
# passengers = [13,10,8,4,12,14,18,19,5,2,30,34]
# capacity = 1
# print(solution.latestTimeCatchTheBus(buses, passengers, capacity)) 
        