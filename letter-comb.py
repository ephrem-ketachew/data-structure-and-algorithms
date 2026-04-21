# 17. Letter Combinations of a Phone Number
# Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(digits)
        res = []
        def backtrack(index: int, current_state: list[str]) -> None:
            if len(current_state) == n:
                res.append(''.join(current_state[:]))
                return
            
            digit = int(digits[index])
            letters = num_char[digit - 2]
            for i in range(len(letters)):
                current_state.append(letters[i])
                backtrack(index + 1, current_state)
                current_state.pop()
                
        backtrack(0, [])
        return res