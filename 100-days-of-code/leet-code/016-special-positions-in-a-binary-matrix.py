# 1582. Special Positions in a Binary Matrix
# Easy

# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 
# (rows and columns are 0-indexed).

 class Solution(object):
    def numSpecial(self, mat):
        specials = 0

        for i in range(len(mat)):
            index = self.checkRow(mat, i)
            if index >= 0 and self.checkColumn(mat, i, index):
                specials += 1

        return specials

    def checkRow(self, mat, i):
        index = -1
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                if index >= 0:
                    return -1
                else:
                    index = j
        return index

    def checkColumn(self, mat, i, index):
        for j in range(len(mat)):
            if mat[j][index] == 1 and j != i:
                return False
        return True
        