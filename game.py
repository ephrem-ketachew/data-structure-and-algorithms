# 679. 24 Game
# Hard

# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

# You are restricted with the following rules:

# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.

# Example 1:

# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
# Example 2:

# Input: cards = [1,2,1,2]
# Output: false
 
# Constraints:

# cards.length == 4
# 1 <= cards[i] <= 9

from typing import List
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        permutations = []
        def backtrack(curr: list, seen: set) -> None:
            if len(curr) == 7:
                permutations.append(curr[:])
                return
            
            if len(curr) % 2 == 0:
                for i in range(4):
                    if i not in seen:
                        curr.append(cards[i])
                        seen.add(i)
                        backtrack(curr, seen)
                        curr.pop()
                        seen.remove(i)
            else:
                for op in ['+', '-', '*', '/']:
                    curr.append(op)
                    backtrack(curr, seen)
                    curr.pop()
                    
        backtrack([], set())
        
        def compute(tokens: list) -> set:            
            if len(tokens) == 1:
                return tokens
            
            vals = set()
            for i, ch in enumerate(tokens):
                if ch in ['+', '-', '*', '/']:
                    left_vals = compute(tokens[:i])
                    right_vals = compute(tokens[i + 1:])
                    for num1 in left_vals:
                        val = None
                        for num2 in right_vals:
                            if ch == '+':
                                val = num1 + num2
                            elif ch == '-':
                                val = num1 - num2
                            elif ch == '*':
                                val = num1 * num2
                            else:
                                if num2 != 0:
                                    val = num1 / num2
                           
                            if val is not None:     
                                vals.add(val)

            return vals

        for permutation in permutations:      
            for val in compute(permutation): 
                if math.isclose(val, 24):
                    return True
            
        return False
