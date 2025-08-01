# 640. Solve the Equation
# Medium
# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

# Example 1:

# Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:

# Input: equation = "x=x"
# Output: "Infinite solutions"
# Example 3:

# Input: equation = "2x=x"
# Output: "x=0"

# Constraints:

# 3 <= equation.length <= 1000
# equation has exactly one '='.
# equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
# The input is generated that if there is a single solution, it will be an integer.

class Solution:
    def solveEquation(self, equation: str) -> str:
        def calc_side(side):
            def get_value(term):
                if term == '' or term == '+':
                    return 1
                elif term == '-':
                    return -1
                return int(term)
            
            term = ''
            x = value = 0
            for ch in side:
                if (ch != '+' and ch != '-') or not term:
                    term += ch
                else:
                    if 'x' in term:
                        x += get_value(term[:-1])
                    else:
                        value += get_value(term)
                    term = ch        
            if 'x' in term:
                x += get_value(term[:-1])
            else:
                value += get_value(term)
                
            return x, value
                
        x = value = 0
        left_side, right_side = equation.split('=')
        
        var, val = calc_side(left_side)
        x += var
        value -= val
        
        var, val = calc_side(right_side)
        x -= var
        value += val
        
        if x != 0:
            return f'x={value // x}'
        elif value == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
        
# solution = Solution()
# equation = "x+5-3+x=6+x-2"
# equation = "x=x"
# equation = "2x=x"
# equation = "-x=1"
# print(solution.solveEquation(equation))