# 726. Number of Atoms
# Hard

# Given a string formula representing a chemical formula, return the count of each atom.

# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.

# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.

# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# The test cases are generated so that all the values in the output fit in a 32-bit integer.

# Example 1:

# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:

# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:

# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

# Constraints:

# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.

from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        decimal = []
        for i, ch in enumerate(formula):
            if ch.islower():
                stack[-1] = stack[-1] + ch
                
            elif ch == ')' and (i == len(formula) - 1 or not formula[i + 1].isdecimal()):
                buffer = []
                while stack[-1] != '(':
                    buffer.append(stack.pop())
                stack.pop()
                while buffer:
                    stack.append(buffer.pop())
                
            elif ch.isdecimal():
                decimal.append(ch)
                if i + 1 < len(formula) and formula[i + 1].isdecimal():
                    continue
                
                num = int(''.join(decimal))
                if stack[-1] == ')':
                    stack.pop()
                    cur_counter = Counter()
                    while stack[-1] != '(':
                        cur_ch = stack.pop()
                        if cur_ch.isdecimal():
                            atom = stack.pop()
                            cur_counter[atom] += int(cur_ch) * num
                        else:
                            atom = cur_ch
                            cur_counter[atom] += num
                        
                    stack.pop()
                    for key in cur_counter:
                        stack.append(key)
                        if cur_counter[key] > 1:
                            stack.append(str(cur_counter[key]))
                        
                else:
                    stack.append(str(num))
                    
                decimal = []
            else:
                stack.append(ch)
                
        counter = Counter()
        while stack:
            ch = stack.pop()
            if ch == '(' or ch == ')':
                continue
            if ch.isdecimal():
                atom = stack.pop()
                counter[atom] += int(ch)
            else:
                counter[ch] += 1
                
        keys = sorted(counter.keys())
        ans = []
        for key in keys:
            ans.append(key)
            if counter[key] > 1:
                ans.append(str(counter[key]))
                
        return ''.join(ans)