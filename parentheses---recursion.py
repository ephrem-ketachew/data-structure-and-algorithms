# 241. Different Ways to Add Parentheses
# Medium

# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].
# The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        for i, ch in enumerate(expression):
            if ch in '*-+':
                left_expression = expression[:i]
                right_expression = expression[i + 1:]
                
                left_res = self.diffWaysToCompute(left_expression)
                right_res = self.diffWaysToCompute(right_expression)
                
                for l in left_res:
                    for r in right_res:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
                            
        if len(res) == 0:
            res.append(int(expression))
                
        return res