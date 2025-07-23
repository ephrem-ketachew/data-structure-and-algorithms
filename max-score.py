# 1717. Maximum Score From Removing Substrings
# Medium
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20

# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def get_score(x, y, a, b):
            stack1 = []
            stack2 = []
            score = 0
            for ch in s:
                if ch == b and stack1 and stack1[-1] == a:
                    stack1.pop()
                    score += x
                else:
                    stack1.append(ch)

            for ch in stack1:
                if ch == a and stack2 and stack2[-1] == b:
                    stack2.pop()
                    score += y
                else:
                    stack2.append(ch)
                    
            return score
                    
        return get_score(x, y, 'a', 'b') if x >= y else get_score(y, x, 'b', 'a')
                    
                    
# solution = Solution()
# s = "cdbcbbaaabab"
# x = 4
# y = 5
# s = "aabbaaxybbaabb"
# x = 5
# y = 4
# print(solution.maximumGain(s, x, y))