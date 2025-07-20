# 423. Reconstruct Original Digits from English
# Medium
# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

# Example 1:

# Input: s = "owoztneoer"
# Output: "012"
# Example 2:

# Input: s = "fviefuro"
# Output: "45"

# Constraints:

# 1 <= s.length <= 105
# s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
# s is guaranteed to be valid.

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        uniques = [
            ['z', 'zero', '0'], 
            ['w', 'two', '2'], 
            ['x', 'six', '6'], 
            ['g', 'eight', '8'], 
            ['s', 'seven', '7'], 
            ['u', 'four', '4'], 
            ['t', 'three', '3'], 
            ['v', 'five', '5'], 
            ['i', 'nine', '9'], 
            ['o', 'one', '1'], 
        ]
        
        left = 0
        res = ''
        while len(counter) > 0:
            if uniques[left][0] in counter:
                count = counter[uniques[left][0]]
                res += count * uniques[left][2]
                num = uniques[left][1]
                for i in range(len(num)):
                    ch = num[i]
                    counter[ch] -= count
                    if counter[ch] == 0:
                        del counter[ch]
            left += 1
            
        res = sorted(res)
        
        return ''.join(res)
        
# solution = Solution()
# s = "owoztneoer"
# s = "fviefuro"
# s = "zerozero"
# print(solution.originalDigits(s))