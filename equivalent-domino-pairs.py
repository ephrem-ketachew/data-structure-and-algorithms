# 1128. Number of Equivalent Domino Pairs

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

# Example 2:
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # eqv_pairs = 0
        # for i in range(len(dominoes) - 1):
        #     for j in range(i + 1, len(dominoes)):
        #         if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
        #             eqv_pairs += 1
        #             print(dominoes[i])
        # return eqv_pairs
        pairs = dict()
        for i in range(len(dominoes)):
            dominoes[i].sort()
            pair = tuple(dominoes[i])
            pairs[pair] = pairs.get(pair, 0) + 1
        
        eqv_pairs = 0
        for freq in pairs.values():
            eqv_pairs += int(freq * (freq - 1) / 2)
        return eqv_pairs
