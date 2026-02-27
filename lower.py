# 709. To Lower Case
# Easy

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

# Constraints:

# 1 <= s.length <= 100
# s consists of printable ASCII characters.

class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(ch) + 32) if 65 <= ord(ch) < 65 + 26 else ch  for ch in s])