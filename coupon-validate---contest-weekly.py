# Q1. Coupon Code Validator
# Easy
# 3 pt.
# You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

# code[i]: a string representing the coupon identifier.
# businessLine[i]: a string denoting the business category of the coupon.
# isActive[i]: a boolean indicating whether the coupon is currently active.
# A coupon is considered valid if all of the following conditions hold:

# code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
# isActive[i] is true.
# Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

# Example 1:

# Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

# Output: ["PHARMA5","SAVE20"]

# Explanation:

# First coupon is valid.
# Second coupon has empty code (invalid).
# Third coupon is valid.
# Fourth coupon has special character @ (invalid).
# Example 2:

# Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

# Output: ["ELECTRONICS_50"]

# Explanation:

# First coupon is inactive (invalid).
# Second coupon is valid.
# Third coupon has invalid business line (invalid).

# Constraints:

# n == code.length == businessLine.length == isActive.length
# 1 <= n <= 100
# 0 <= code[i].length, businessLine[i].length <= 100
# code[i] and businessLine[i] consist of printable ASCII characters.
# isActive[i] is either true or false.©leetcode

from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_businessLines = [ "electronics", "grocery", "pharmacy", "restaurant"]
        
        output = []
        
        for i in range(len(code)):
            isValid = True if isActive[i] and code[i] and businessLine[i] in valid_businessLines else False
            if not isValid:
                continue
            
            if not re.fullmatch(r'[A-Za-z0-9_]+', code[i]):
                isValid = False
            # for char in code[i]:
            #     if not (char.isalnum() or char == '_'):
            #         isValid = False
            #         break
            
            if isValid:
                output.append((code[i], businessLine[i]))
                
        sorted_codes = sorted(
            output, 
            key=lambda t:(
                valid_businessLines.index(t[1]),
                t[0]
                )
            )                
        
        return [t[0] for t in sorted_codes]
    
# solution = Solution()
# code = ["SAVE20","","PHARMA5","SAVE@20"]
# businessLine = ["restaurant","grocery","pharmacy","restaurant"]
# isActive = [True,True,True,True]

# code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
# businessLine = ["grocery","electronics","invalid"]
# isActive = [False,True,True]

# code = ["W"]
# businessLine = ["invalid"]
# isActive = [True]
# print(solution.validateCoupons(code, businessLine, isActive))