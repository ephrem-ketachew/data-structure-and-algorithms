# 3443. Maximum Manhattan Distance After K Changes

# You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

# 'N' : Move north by 1 unit.
# 'S' : Move south by 1 unit.
# 'E' : Move east by 1 unit.
# 'W' : Move west by 1 unit.
# Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

# Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

# The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

# Example 1:

# Input: s = "NWSE", k = 1

# Output: 3

# Explanation:

# Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

# Movement	Position (x, y)	Manhattan Distance	Maximum
# s[0] == 'N'	(0, 1)	0 + 1 = 1	1
# s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
# s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
# s[3] == 'E'	(0, 2)	0 + 2 = 2	3
# The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

# Example 2:

# Input: s = "NSWWEW", k = 3

# Output: 6

# Explanation:

# Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

# The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

class Solution:
    def maxDistance(self, s: str, k: int) -> int: 
        max_manhattan_distance = 0       
        for direction in ['NE', 'NW', 'SE', 'SW']:
            manhattan_distance = 0
            maximum = 0
            x, y = 0, 0
            k_move = k
            moves = list(s)
            
            for i in range(len(moves)):
                if k_move > 0:
                    if direction == 'NE':
                        if moves[i] == 'S':
                            moves[i] = 'N'
                            k_move -= 1
                        elif moves[i] == 'W':
                            moves[i] = 'E'
                            k_move -= 1
                    elif direction == 'NW':
                        if moves[i] == 'S':
                            moves[i] = 'N'
                            k_move -= 1
                        elif moves[i] == 'E':
                            moves[i] = 'W'
                            k_move -= 1
                    elif direction == 'SW':
                        if moves[i] == 'N':
                            moves[i] = 'S'
                            k_move -= 1
                        elif moves[i] == 'E':
                            moves[i] = 'W'
                            k_move -= 1
                    else:
                        if moves[i] == 'N':
                            moves[i] = 'S'
                            k_move -= 1
                        elif moves[i] == 'W':
                            moves[i] = 'E'
                            k_move -= 1
                            
                if moves[i] == 'N':
                    y += 1
                elif moves[i] == 'S':
                    y -= 1
                elif moves[i] == 'E':
                    x += 1
                else:
                    x -= 1
                
                manhattan_distance = abs(x) + abs(y)
                maximum = max(maximum, manhattan_distance)
            
            max_manhattan_distance = max(max_manhattan_distance, maximum)
        
        return max_manhattan_distance
        
        
        
        # def __maxDistance(direction, s, k):
        #     my_counter = Counter(s)
        #     y_change = min(my_counter['N'], my_counter['S'])
        #     x_change = min(my_counter['E'], my_counter['W'])
            
        #     allowed_x = allowed_y = 0
        #     if direction == 'y':
        #         if k > y_change:
        #             allowed_y = y_change
        #             k = k - y_change
        #             if k > x_change:
        #                 allowed_x = x_change
        #             else:
        #                 allowed_x = k
        #         else:
        #             allowed_y = k
        #     else:
        #         if k > x_change:
        #             allowed_x = x_change
        #             k = k - x_change
        #             if k > y_change:
        #                 allowed_y = y_change
        #             else:
        #                 allowed_y = k
        #         else:
        #             allowed_x = k
                    
        #     if my_counter['N'] == y_change:
        #         old_value_y = 'N'
        #         new_value_y = 'S'
        #     else:
        #         old_value_y = 'S'
        #         new_value_y = 'N'
                
        #     if my_counter['E'] == x_change:
        #         old_value_x = 'E'
        #         new_value_x = 'W'
        #     else:
        #         old_value_x = 'W'
        #         new_value_x = 'E'
            
        #     s = s.replace(old_value_y, new_value_y, allowed_y)      
        #     s = s.replace(old_value_x, new_value_x, allowed_x)
            
        #     manhattan_distance = 0
        #     maximum = 0
        #     x, y = 0, 0
            
        #     for i in range(len(s)):
        #         if s[i] == 'N':
        #             y += 1
        #         elif s[i] == 'S':
        #             y -= 1
        #         elif s[i] == 'E':
        #             x += 1
        #         else:
        #             x -= 1
                
        #         manhattan_distance = abs(x) + abs(y)
        #         maximum = max(maximum, manhattan_distance)
                
        #     return maximum
        
        # return max(__maxDistance('y', s, k), __maxDistance('x', s, k))
    
# s = Solution()
# print(s.maxDistance("NSWWEW", 3))