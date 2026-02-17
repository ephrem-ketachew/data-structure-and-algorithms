# 2528. Maximize the Minimum Powered City
# Hard

# You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

# Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

# Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
# The power of a city is the total number of power stations it is being provided power from.

# The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

# Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

# Note that you can build the k power stations in multiple cities.

# Example 1:

# Input: stations = [1,2,4,5,0], r = 1, k = 2
# Output: 5
# Explanation: 
# One of the optimal ways is to install both the power stations at city 1. 
# So stations will become [1,4,4,5,0].
# - City 0 is provided by 1 + 4 = 5 power stations.
# - City 1 is provided by 1 + 4 + 4 = 9 power stations.
# - City 2 is provided by 4 + 4 + 5 = 13 power stations.
# - City 3 is provided by 5 + 4 = 9 power stations.
# - City 4 is provided by 5 + 0 = 5 power stations.
# So the minimum power of a city is 5.
# Since it is not possible to obtain a larger power, we return 5.
# Example 2:

# Input: stations = [4,4,4,4], r = 0, k = 3
# Output: 4
# Explanation: 
# It can be proved that we cannot make the minimum power of a city greater than 4.
 

# Constraints:

# n == stations.length
# 1 <= n <= 105
# 0 <= stations[i] <= 105
# 0 <= r <= n - 1
# 0 <= k <= 109

from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        current_window = sum(stations[:r+1])
        power[0] = current_window
        for i in range(1, n):
            if i + r < n:
                current_window += stations[i + r]
            if i - r - 1 >= 0:
                current_window -= stations[i - r - 1]
                
            power[i] = current_window
        
        def check(target: int) -> bool:
            current_added_power = 0
            stations_added = 0
            
            expires = [0] * n
            for i in range(n):
                current_added_power -= expires[i]
                actual_power = power[i] + current_added_power
                
                if actual_power < target:
                    needed = target - actual_power
                    stations_added += needed
                    if stations_added > k:
                        return False
                    
                    current_added_power += needed
                    
                    next_expires_at = i + 2 * r + 1
                    if next_expires_at < n:
                        expires[next_expires_at] += needed
                        
            return True
        
        low = min(power)
        high = min(power) + k
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
        