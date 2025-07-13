# 1769. Minimum Number of Operations to Move All Balls to Each Box
# Medium
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
# Example 2:

# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]

# Constraints:

# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # prefix = [0] * len(boxes)
        # suffix = [0] * len(boxes)
        # for i in range(1, len(boxes)):
        #     cost = 0
        #     for j in range(i - 1, -1, -1):
        #         if boxes[j] == '1':
        #             cost += (i - j)
        #     prefix[i] = cost
                    
        # for i in range(len(boxes) - 2, -1, -1):
        #     cost = 0
        #     for j in range(i + 1, len(boxes)):
        #         if boxes[j] == '1':
        #             cost += (j - i)
        #     suffix[i] = cost
            
        # total_cost = [0] * len(boxes)
        # for i in range(len(boxes)):
        #     total_cost[i] = prefix[i] + suffix[i]
            
        # return total_cost
        
        res = [0] * len(boxes)
        
        ops = 0
        balls = 0
        for i in range(len(boxes)):
            res[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls
            
        ops = 0
        balls = 0    
        for i in range(len(boxes) - 1, -1, -1):
            res[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls
            
        return res
        