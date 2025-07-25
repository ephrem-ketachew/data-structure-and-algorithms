# 925. Long Pressed Name
# Easy
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# Example 1:

# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:

# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 
# Constraints:

# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # if len(name) > len(typed):
        #     return False
        
        # j = 0
        # for i in range(len(typed)):
        #     if j == len(name):
        #         if name[-1] != typed[i]:
        #             return False
        #     elif typed[i] == name[j]:
        #         j += 1
        #     else:
        #         if i - 1 < 0 or typed[i] != typed[i - 1]:
        #             return False
                
        # return True if j == len(name) else False
        
        i = j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
            
        return i == len(name)
    
# solution = Solution()
# name = "alex"
# typed = "aaleex"
# name = "saeed"
# typed = "ssaaedd"
# name = "pyplrz"
# typed = "ppyypllr"
# print(solution.isLongPressedName(name, typed))