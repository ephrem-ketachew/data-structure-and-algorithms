# 2582. Pass the Pillow
# Easy
# There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

# For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

# Example 1:

# Input: n = 4, time = 5
# Output: 2
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
# After five seconds, the 2nd person is holding the pillow.
# Example 2:

# Input: n = 3, time = 2
# Output: 3
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
# After two seconds, the 3rd person is holding the pillow.

# Constraints:

# 2 <= n <= 1000
# 1 <= time <= 1000
 
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # direction = 1
        # person = 1
        # for i in range(time):
        #     if person == n:
        #         direction = -1
        #     if person == 1:
        #         direction = 1
                
        #     person += direction
            
        # return person
        
        cycle = time % (2 * (n - 1))
        return cycle + 1 if cycle < n else 2 * n - cycle - 1
    
    
    