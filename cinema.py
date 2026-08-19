# 1386. Cinema Seat Allocation
# Medium

# A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

# You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

# A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

#0123456789
#1234
#5678
#3456


# seats 2, 3, 4, 5
# seats 4, 5, 6, 7
# seats 6, 7, 8, 9
# A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

# Return an integer denoting the maximum number of four-person groups that can be assigned.

# Example 1:

# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
# Example 2:

# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# Example 3:

# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4

# Constraints:

# 1 <= n <= 109
# 1 <= reservedSeats.length <= min(10 * n, 104)
# reservedSeats[i] == [rowi, seati]
# 1 <= rowi <= n
# 1 <= seati <= 10
# All reservedSeats[i] are distinct.

from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def check_block(start: int, row: int) -> bool:
            for i in range(start, start + 4):
                if (1 << i) & seats[row] != 0:
                    return False
            return True 
                
        seats = defaultdict(int)
        reserved_rows = set()
        for row, seat in reservedSeats:
            seats[row] |= 1 << (seat - 1)
            reserved_rows.add(row)
            
        count = 2 * (n - len(reserved_rows))
        for row in seats:
            block1 = check_block(1, row)
            block2 = check_block(3, row)
            block3 = check_block(5, row)
            if block1:
                count += 1
            if block3:
                count += 1
            if not block1 and not block3 and block2:
                count += 1
                
        return count