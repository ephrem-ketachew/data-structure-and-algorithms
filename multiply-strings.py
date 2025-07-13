# 43. Multiply Strings
# Medium
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = []
          
        for i in range(len(num1) - 1, -1, -1):
            num = int(num1[i])
            
            carry, temp = 0, []
            for j in range(len(num2) - 1, -1, -1):
                r = num * int(num2[j]) + carry
                carry = r // 10
                temp.append(str(r % 10))
            if carry > 0:
                temp.append(str(carry))
            temp = temp[::-1] + ['0'] * (len(num1) - 1 - i)
            
            if not res:
                res = temp
            else:
                carry, summ = 0, 0
                for k in range(- 1, -len(temp)- 1, -1):
                    if k < -len(res):
                        break
                    summ = int(temp[k]) + int(res[k]) + carry
                    carry = summ // 10
                    if k >= -len(res):
                        res[k] = str(summ % 10)
                
                rest = []
                for l in range(-len(res) - 1, -len(temp)- 1, -1):
                    summ = int(temp[l]) + carry
                    carry = summ // 10
                    rest = [str(summ % 10)] + rest
                    
                if carry:
                    rest = [str(carry)] + rest
                    
                res = rest + res
            
        return ''.join(res)
    
# solution = Solution()
# num1 = "2"
# num2 = "3"
# num1 = "123"
# num2 = "456"

# num1 = "98"
# num2 = "9"

# num1 = "999"
# num2 = "999"

# num1 = "408"
# num2 = "5"
# print(solution.multiply(num1, num2))
                