# 1324. Print Words Vertically
# Medium

# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word. 

# Example 1:

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
#  "HAY"
#  "ORO"
#  "WEU"
# Example 2:

# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"
# Example 3:

# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]

# Constraints:

# 1 <= s.length <= 200
# s contains only upper case English letters.
# It's guaranteed that there is only one space between 2 words.

from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        s_arr = s.split()
        i = 0
        while True:
            word = []
            for j in range(len(s_arr)):
                if i < len(s_arr[j]):
                    word.append(s_arr[j][i])
                else:
                    word.append(' ')
                    
            k = len(word) - 1
            while k >= 0 and word[k] == ' ':
                word.pop()
                k -= 1
                
            if word:
                ans.append(''.join(word))
            else:
                break
            
            i += 1
            
        return ans