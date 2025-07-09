# 859. Buddy Strings
# Easy

# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:

# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
# Example 2:

# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
# Example 3:

# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# Constraints:

# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == 1 or len(s) != len(goal):
            return False
        
        index1, index2 = -1, -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if index1 == -1:
                    index1 = i
                elif index2 == -1:
                    index2 = i
                else:
                    return False
                
        if index1 == index2 == -1:
            return len(set(s)) < len(s)
        
        if index1 == -1 or index2 == -1:
            return False
        
        return s[index1] == goal[index2] and s[index2] == goal[index1]