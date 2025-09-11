# 3403. Find the Lexicographically Largest String From the Box I
# Medium
# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.


# Example 1:

# Input: word = "dbca", numFriends = 2

# Output: "dbc"

# Explanation: 

# All possible splits are:

# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:

# Input: word = "gggg", numFriends = 4

# Output: "g"

# Explanation: 

# The only possible split is: "g", "g", "g", and "g".

# Constraints:

# 1 <= word.length <= 5 * 103
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # def is_larger(start, end, target):
        #     i, j = start, 0
        #     while i < end and j < len(target):
        #         if word[i] > target[j]:
        #             return True
        #         if word[i] < target[j]:
        #             return False
        #         i += 1
        #         j += 1
        #     return i < end
        
        # max_len = len(word) - numFriends + 1
        # max_word = word[:max_len]
        # if max_len == len(word):
        #     return word
        # for i in range(len(word)):
        #     for j in range(i, min(i + max_len, len(word))):
        #         if is_larger(i, j + 1, max_word):
        #             max_word = word[i:j + 1]
                
        # return max_word
        
        max_len = len(word) - numFriends + 1
        if max_len == len(word):
            return word
        max_word = word[:max_len]
        for i in range(len(word)):
            max_word = max(max_word, word[i:i+max_len])
            
        return max_word
    
# solution = Solution()
# word = "dbca"
# numFriends = 2
# print(solution.answerString(word, numFriends))