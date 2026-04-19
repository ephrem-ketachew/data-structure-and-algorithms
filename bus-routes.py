# 815. Bus Routes
# Hard

# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1

# Constraints:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 105
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 105
# 0 <= routes[i][j] < 106
# 0 <= source, target < 106

from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # bus_stations = defaultdict(set)
        # for route in routes:
        #     route = set(route)
        #     for station in route:
        #         bus_stations[station].update(route)
                
        # queue = deque([source])
        # seen = set([source])
        # bus_count = 1
        # while queue:
        #     t = len(queue)
        #     for _ in range(t):
        #         station = queue.popleft()
        #         if target in bus_stations[station]:
        #             return bus_count
                
        #         for s in bus_stations[station]:
        #             if s not in seen:
        #                 queue.append(s)
        #                 seen.add(s)
                        
        #     bus_count += 1
                        
        # return -1
        
        station_bus = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for station in route:
                station_bus[station].append(bus_id)
                
        queue = deque([(source, 0)])
        seen_buses = set()
        seen_stations = set([source])
        while queue:
            station, buses_taken = queue.popleft()
            if station == target:
                return buses_taken
            
            for bus_id in station_bus[station]:
                if bus_id not in seen_buses:
                    seen_buses.add(bus_id)
                    for next_station in routes[bus_id]:
                        if next_station not in seen_stations:
                            seen_stations.add(next_station)
                            queue.append((next_station, buses_taken + 1))
                            
        return -1