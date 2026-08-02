# 2266. Count Number of Texts
# Medium

# Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.

# In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

# For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
# Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
# However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

# For example, when Alice sent the message "bob", Bob received the string "2266622".
# Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:

# Input: pressedKeys = "22233"
# Output: 8
# Explanation:
# The possible text messages Alice could have sent are:
# "aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
# Since there are 8 possible messages, we return 8.
# Example 2:

# Input: pressedKeys = "222222222222222222222222222222222222"
# Output: 82876089
# Explanation:
# There are 2082876103 possible text messages Alice could have sent.
# Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.

# Constraints:

# 1 <= pressedKeys.length <= 105
# pressedKeys only consists of digits from '2' - '9'.

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7
        def count_same_chars(num: str, n: int) -> int:
            if num == '7' or num == '9':
                if n <= 2:
                    return n
                if n == 3:
                    return 4
                
                p1, p2, p3, p4 = 1, 1, 2, 4
                i = 3
                while i < n:
                    p1, p2, p3, p4 = p2, p3, p4, (p1 + p2 + p3 + p4) % MOD
                    i += 1
                
                return p4
            
            if n <= 2:
                return n
            
            p1, p2, p3 = 1, 1, 2
            i = 2
            while i < n:
                p1, p2, p3 = p2, p3, (p1 + p2 + p3) % MOD
                i += 1
            
            return p3
        
        count = 1
        pressedKeys += 'a'
        prev = pressedKeys[0]
        curr_cnt = 0
        for char in pressedKeys:
            if char == prev:
                curr_cnt += 1
            else:
                count = (count * count_same_chars(prev, curr_cnt)) % MOD
                curr_cnt = 1
                prev = char
                
        return count
    
s = Solution()
pressedKeys = "22233"
# pressedKeys = "222222222222222222222222222222222222"
# pressedKeys = '222'
# pressedKeys = '2222'
print(s.countTexts(pressedKeys))