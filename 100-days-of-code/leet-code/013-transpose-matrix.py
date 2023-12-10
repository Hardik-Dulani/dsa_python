# 867. Transpose Matrix
# Easy

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.transpose(matrix)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return result

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return zip(*matrix)