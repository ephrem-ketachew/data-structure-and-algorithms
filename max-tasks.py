# 2071. Maximum Number of Tasks You Can Assign
# Hard

# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed. 

# Example 1:

# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)
# Example 2:

# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 0 (0 + 5 >= 5)
# Example 3:

# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# Output: 2
# Explanation:
# We can assign the magical pills and tasks as follows:
# - Give the magical pill to worker 0 and worker 1.
# - Assign worker 0 to task 0 (0 + 10 >= 10)
# - Assign worker 1 to task 1 (10 + 10 >= 15)
# The last pill is not given because it will not make any worker strong enough for the last task.
 

# Constraints:

# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 104
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 109

from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # A FAILED ATTEMPT
        # n, m = len(tasks), len(workers)
        
        # tasks.sort(reverse=True)
        # workers.sort(reverse=True)
        
        # i = j = 0
        # remaining_task = []
        # while i < n and j < m:
        #     if workers[j] >= tasks[i]:
        #         i += 1
        #         j += 1
        #     else:
        #         remaining_task.append(tasks[i])
        #         i += 1
            
        # i = 0    
        # while pills > 0 and j < m and i < len(remaining_task):
        #     if workers[j] + strength >= remaining_task[i]:
        #         i += 1
        #         j += 1
        #         pills -= 1
        #     else:
        #         i += 1
                
        # return j
        
        workers.sort()
        tasks.sort()
        
        def check(k: int):
            pills_left = pills
            cur_workers = workers[-k:]
            cur_tasks = tasks[:k]
            
            j = k - 1
            available_workers = deque()
            for i in range(k - 1, -1, -1):
                while j >= 0 and cur_workers[j] + strength >= cur_tasks[i]:
                    available_workers.appendleft(cur_workers[j])
                    j -= 1
                    
                if not available_workers:
                    return False
                    
                if available_workers[-1] >= cur_tasks[i]:
                    available_workers.pop()
                else:
                    if pills_left > 0:
                        available_workers.popleft()
                        pills_left -= 1
                    else:
                        return False
                    
            return True
        
        low = 0
        high = min(len(tasks), len(workers))
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
                    