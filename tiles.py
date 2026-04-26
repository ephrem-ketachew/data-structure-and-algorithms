# 1079. Letter Tile Possibilities
# Medium

# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

# Example 1:

# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: tiles = "AAABBC"
# Output: 188
# Example 3:

# Input: tiles = "V"
# Output: 1

# Constraints:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        self.count = 0
        n = len(tiles)
        def backtrack(curr: str, seen: set[int]) -> None:
            self.count += 1      
            if len(curr) == n:
                return
            
            for i, ch in enumerate(tiles):
                if (i in seen) or (i > 0 and (i - 1 not in seen) and ch == tiles[i - 1]):
                    continue
                
                seen.add(i)
                backtrack(curr + ch, seen)
                seen.remove(i)
                
        backtrack('', set())
        return self.count - 1