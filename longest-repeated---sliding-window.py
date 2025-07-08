# 1156. Swap For Longest Repeated Character Substring
# Medium
# You are given a string text. You can swap two of the characters in the text.

# Return the length of the longest substring with repeated characters.

# Example 1:

# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
# Example 2:

# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
# Example 3:

# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.

# Constraints:

# 1 <= text.length <= 2 * 104
# text consist of lowercase English characters only.

from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # where i tried to use sliding window cause the question is tagged sliding window .... i get ac and beat only 15%..it turns out sliding window isn't the right technique here ...it make things complicated and inefficient due to the need to handle multiple edge cases...
        # left = 0
        # max_len = 1
        # count = Counter(text[0])
        
        # for right in range(1, len(text)):
        #     count[text[right]] += 1
        #     while len(count) > 2:
        #         count[text[left]] -= 1
        #         if count[text[left]] == 0:
        #             del count[text[left]]
        #         left += 1
                
        #     while len(count) > 1 and min(count.values()) > 1:
        #         count[text[left]] -= 1
        #         if count[text[left]] == 0:
        #             del count[text[left]]
        #         left += 1
                
    
        #     max_val = max(count.values())
        #     for c in count:
        #         if count[c] == max_val:
        #             char = c  
                    
        #     if len(count) > 1 and not (char in text[:left] or char in text[right + 1:]):
        #         left = right
        #         count = Counter(text[left])
    
        #     max_len = max(max_len, right - left + 1)
            
        # return max_len
        
        
        # here is the right approach which is efficient and readable
        n = len(text)
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j
            
        count = Counter(text)
        max_len = 0
        for i, (char, length) in enumerate(groups):
            max_len = max(max_len, min(length + 1, count[char]))
            
            if i + 2 < len(groups) and groups[i + 1][1] == 1 and groups[i][0] == groups[i + 2][0]:
                merged_len = length + groups[i + 2][1]
                if count[char] > merged_len:
                    merged_len += 1
                    
                max_len = max(max_len, merged_len)
                
        return max_len
    
# solution = Solution()
# text = "ababa"
# text = "aaabaaa"
# text = "aaaaa"
# print(solution.maxRepOpt1(text))