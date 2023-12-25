

# Given a square matrix of size n*n. The task is to find the determinant of this matrix.
#User function Template for python3
class Solution:
    
    #Function to get cofactor of matrix[p][q] in temp[][].
    def getCofactor(self,matrix, temp, p, q, n):
        
        i,j = 0,0
        for row in range(n):
            for col in range(n):
                
                #copying only those elements into temporary matrix 
                #which are not in given row and column.
                if row != p and col != q:
                    temp[i][j] = matrix[row][col]
                    j+=1
    
                    #if row is filled, we increase row index and
                    #reset column index.
                    if j==n-1:
                        j=0
                        i+=1
    
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        
        d = 0 
        #base case 
        if n==1:
            return matrix[0][0]
    
        #creating a list to store Cofactors.
        temp = [ [0 for i in range(n)] for i in range(n)]

        sign = 1
    
        #iterating for each element of first row.
        for i in range(n):
    
            #getting Cofactor of matrix[0][i].
            self.getCofactor(matrix, temp, 0, i, n)
            d += sign * matrix[0][i] * self.determinantOfMatrix(temp,n-1)
    
            #terms are to be added with alternate sign so changing the sign.
            sign = -sign 
    
        #returning the determinant.
        return d
