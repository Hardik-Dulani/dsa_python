# Anti Diagonal Traversal of Matrix
# MediumAccuracy: 73.72%
# Give a N*N square matrix, 
# return an array of its anti-diagonals in top-leftmost to bottom-rightmost order. 
# In an element of a anti-diagonal (i, j), surrounding elements will be (i+1, j-1) and (i-1, j+1). Look at the examples for more clarity.




class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        ar=[]
        key=0
        n=len(matrix)
        for i in range((n-1)*2+1):
            for i in range(n):
                for j in range(n):
                    if i + j == key:
                        ar.append(matrix[i][j])
            key+=1
        return ar
