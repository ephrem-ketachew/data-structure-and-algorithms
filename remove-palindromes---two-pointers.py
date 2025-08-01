# 1332. Remove Palindromic Subsequences
# Easy
# You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

# Return the minimum number of steps to make the given string empty.

# A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does not necessarily need to be contiguous.

# A string is called palindrome if is one that reads the same backward as well as forward.

# Example 1:

# Input: s = "ababa"
# Output: 1
# Explanation: s is already a palindrome, so its entirety can be removed in a single step.
# Example 2:

# Input: s = "abb"
# Output: 2
# Explanation: "abb" -> "bb" -> "". 
# Remove palindromic subsequence "a" then "bb".
# Example 3:

# Input: s = "baabb"
# Output: 2
# Explanation: "baabb" -> "b" -> "". 
# Remove palindromic subsequence "baab" then "b".
 
# Constraints:

# 1 <= s.length <= 1000
# s[i] is either 'a' or 'b'.

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # CHAPTER ONE -- IGNORANCE, FALSE ASSUMPTION, WRONG APPROACH, TEDIOUS WORK, WASTED AN HOUR😭, DROPPED MY CONFIDENCE
        
        # removed_indices = set()
        # length = len(s)
        # count = 0
        # while length > 0:
        #     left, right = 0, len(s) - 1
        #     while left in removed_indices:
        #         left += 1
        #     while right in removed_indices:
        #         right -= 1
        #     while left <= right:
        #         if s[left] == s[right]:
                    
        #             removed_indices.add(left)
        #             removed_indices.add(right)
                    
        #             if left != right:
        #                 length -= 2
        #             else:
        #                 length -= 1
                    
        #             left += 1
        #             while left in removed_indices:
        #                 left += 1
        #             right -= 1
        #             while right in removed_indices:
        #                 right -= 1
        #         else:
        #             right -= 1
        #             while right in removed_indices:
        #                 right -= 1
        #     count += 1
            
        # return count
        
        # CHAPTER TWO --- WRONG SUBMISSION ON TEST CASE 30/48 BY THE STRING s = "abbaaaab"... I THOUGHT THE LEETCODE IS WRONG ... WONDERING WHY 2 NOT 3.... SO I ASKED AND WHEN I SAW THE STEPS..... MY MIND WAS LIKE🤯 ... I QUICKLY REALIZED THAT THE ANSWER IS EITHER 1 OR 2.... THE QUESTION IS DIFFICULT TILL YOU REALIZE THIS FACT
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1
            
        return 1
    
# solution = Solution()
# s = "ababa"
# s = "abb"
# s = "baabb"
# s = "abbaaaab"
# print(solution.removePalindromeSub(s))