# 854. K-Similar Strings
# Hard

# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

# Example 1:

# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
# Example 2:

# Input: s1 = "abc", s2 = "bca"
# Output: 2
# Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".

# Constraints:

# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
# s2 is an anagram of s1.

from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = deque([s1])
        seen = set([s1])
        k = 0
        while queue:
            t = len(queue)
            for _ in range(t):
                s = queue.popleft()
                if s == s2:
                    return k
                
                arr = list(s)
                i = 0
                while arr[i] == s2[i]:
                    i += 1
                    
                for j in range(i + 1, len(s)):
                    if arr[j] == s2[i] and arr[j] != s2[j]:
                        arr[j], arr[i] = arr[i], arr[j]
                        new_s = ''.join(arr)
                        if new_s not in seen:
                            seen.add(new_s)
                            queue.append(new_s)
                            
                        arr[i], arr[j] = arr[j], arr[i]
                      
            k += 1
            
        return -1