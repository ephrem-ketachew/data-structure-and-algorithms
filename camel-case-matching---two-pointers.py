# 1023. Camelcase Matching
# Medium
# Topics
# Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

# A query word queries[i] matches pattern if you can insert lowercase English letters into the pattern so that it equals the query. You may insert a character at any position in pattern or you may choose not to insert any characters at all.

# Example 1:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# Example 2:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# Example 3:

# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 
# Constraints:

# 1 <= pattern.length, queries.length <= 100
# 1 <= queries[i].length <= 100
# queries[i] and pattern consist of English letters.

from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # ans = [True] * len(queries)
        
        # for i, query in enumerate(queries):
        #     if len(query) < len(pattern):
        #         ans[i] = False
        #         continue
            
        #     k = 0
        #     for j in range(len(pattern)):
        #         while k < len(query) and query[k] != pattern[j]:
        #             if query[k].isupper():
        #                 ans[i] = False
        #                 break
        #             k += 1
                    
        #         if not ans[i]:
        #             break
                
        #         k += 1
                    
        #     if ans[i]:
        #         if k > len(query) or query[k - 1] != pattern[-1]:
        #             ans[i] = False
        #             continue
        #         for m in range(k, len(query)):
        #             if query[m].isupper():
        #                 ans[i] = False
        #                 break
                    
        # return ans
        
        # A CLEAN, SIMPLE AND EASY TO UNDERSTAND CODE
        def match(query: str):
            i = 0
            for ch in query:
                if i < len(pattern) and pattern[i] == ch:
                    i += 1
                elif ch.isupper():
                    return False
            return i == len(pattern)
        
        return [match(query) for query in queries]
    
# solution = Solution()
# queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# pattern = "FB"
# queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# pattern = "FoBaT"
# print(solution.camelMatch(queries, pattern))