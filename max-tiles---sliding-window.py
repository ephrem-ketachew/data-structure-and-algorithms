# 2271. Maximum White Tiles Covered by a Carpet
# Medium
# You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

# You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

# Return the maximum number of white tiles that can be covered by the carpet.

# Example 1:


# Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
# Output: 9
# Explanation: Place the carpet starting on tile 10. 
# It covers 9 white tiles, so we return 9.
# Note that there may be other places where the carpet covers 9 white tiles.
# It can be shown that the carpet cannot cover more than 9 white tiles.
# Example 2:


# Input: tiles = [[10,11],[1,1]], carpetLen = 2
# Output: 2
# Explanation: Place the carpet starting on tile 10. 
# It covers 2 white tiles, so we return 2.

# Constraints:

# 1 <= tiles.length <= 5 * 104
# tiles[i].length == 2
# 1 <= li <= ri <= 109
# 1 <= carpetLen <= 109
# The tiles are non-overlapping.

from typing import List
# from collections import defaultdict
import bisect

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # The Sliding Window tag shall be removed. If you try to use sliding window approach, here is what happens

        # 31 / 51 testcases passed
        # Memory Limit Exceeded
        # tiles = [[1,1000000000]]
        # carpetLen = 1000000000
        # ************************************************************************
        
        # mapp = defaultdict(int)
        # max_value = 0
        
        # for tile in tiles:
        #     for i in range(tile[0], tile[1] + 1):
        #         mapp[i] = 1
        #     max_value = max(max_value, tile[1])
                
                
        # win_cover = 0
        # for i in range(1, carpetLen + 1):
        #     if mapp[i]:
        #         win_cover += 1
                
        # max_cover = win_cover
        # for i in range(carpetLen + 1, max_value + 1):
        #     if mapp[i]:
        #         win_cover += 1
        #     if mapp[i - carpetLen] == 1:
        #         win_cover -= 1
        #     max_cover = max(max_cover, win_cover)
            
        # return max_cover
        
        
        # **************************************************
        max_cover = 0
        
        tiles.sort()
        
        prefix = [0] * (len(tiles) + 1)
        for i, (start, end) in enumerate(tiles):
            prefix[i + 1] = prefix[i] +  (end - start + 1)
        
        for i, (start, end) in enumerate(tiles):
            carpet_end = start + carpetLen - 1
            
            j = bisect.bisect_right(tiles, [carpet_end, float('inf')], lo=i) - 1
            
            total = prefix[j] - prefix[i]
            
            last_start, last_end = tiles[j]
            partial = min(carpet_end, last_end) - last_start + 1
            
            max_cover = max(max_cover, total + partial)
            
        return max_cover
        
        
        
        
        
# solution = Solution()
# tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]]
# carpetLen = 10

# tiles = [[1,1000000000]]
# carpetLen = 1000000000
# print(solution.maximumWhiteTiles(tiles, carpetLen))