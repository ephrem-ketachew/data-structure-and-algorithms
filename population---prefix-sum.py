# 1854. Maximum Population Year
# Easy
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

# The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

# Return the earliest year with the maximum population.

# Example 1:

# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
# Example 2:

# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.
 

# Constraints:

# 1 <= logs.length <= 100
# 1950 <= birthi < deathi <= 2050

from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # max_pop = 0
        # earliest_year_max = float('inf')
        # for i in range(len(logs)):
        #     pop = 0
        #     for j in range(len(logs)):
        #         if logs[j][0] <= logs[i][0] < logs[j][1]:
        #             pop += 1
                   
        #     if pop > max_pop:
        #         max_pop = pop
        #         earliest_year_max = logs[i][0]
        #     elif pop == max_pop and logs[i][0] < earliest_year_max:
        #         earliest_year_max = logs[i][0]

        # return earliest_year_max
        change = [0] * (2050 - 1950 + 1)
        for birth, death in logs:
            change[birth - 1950] += 1
            change[death - 1950] -= 1
            
        max_pop = pop = 0
        year = 1950
        for i in range(len(change)):
            pop += change[i]
            if pop > max_pop:
                max_pop = pop
                year = 1950 + i
                
        return year
        
    
# solution = Solution()
# logs = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
# logs = [[1950,1961],[1960,1971],[1970,1981]]
# print(solution.maximumPopulation(logs))