# 1886. Determine Whether Matrix Can Be Obtained By Rotation
# Easy

# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

# Example 1:

# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Example 2:

# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
# Example 3:

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

# Constraints:

# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] and target[i][j] are either 0 or 1.

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            n = len(matrix)
            rotated_matrix = [[9] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated_matrix[j][n - i - 1] = matrix[i][j]
                    
            return rotated_matrix
        
        def equal(mat1: List[List[int]], mat2: List[List[int]]) -> bool:
            n = len(mat1)
            for i in range(n):
                for j in range(n):
                    if mat1[i][j] != mat2[i][j]:
                        return False
                    
            return True
        
        for _ in range(4):
            mat = rotate(mat)
            if equal(mat, target):
                return True
            
        return False