class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        m, n = len(num1), len(num2)
        i, j = m - 1, n - 1
        carry = 0
        while i >= 0 and j >= 0:
            sum = int(num1[i]) + int(num2[j]) + carry
            ans.append(str(sum % 10))
            carry = sum // 10
            i -= 1
            j -= 1

        while i >= 0:
            sum = int(num1[i]) + carry
            ans.append(str(sum % 10))
            carry = sum // 10
            i -= 1

        while j >= 0:
            sum = int(num2[j]) + carry
            ans.append(str(sum % 10))
            carry = sum // 10
            j -= 1

        if carry > 0:
            ans.append(str(carry))

        return ''.join(ans)[::-1]

        