# Brackets in Matrix Chain Multiplication
# HardAccuracy: 59.66%
# Given an array p[] of length n used to denote the dimensions of a series of matrices such that 
# the dimension of i'th matrix is p[i] * p[i+1]. There are a total of n-1 matrices. 
# Find the most efficient way to multiply these matrices together. 
# As in MCM, you were returning the most effective count but this time 
# return the string which is formed of A - Z (only Uppercase) denoting matrices & Brackets( "(" ")" ) denoting multiplication symbols. 
# For example, if n =11, the matrixes can be denoted as A - K as n<=26 & brackets as multiplication symbols.

# NOTE:

# Each multiplication is denoted by putting open & closed brackets to the matrices multiplied & also
# Please note that the order of matrix multiplication matters, as matrix multiplication is non-commutative A*B != B*A
# As there can be multiple possible answers, the console would print "True" for the
# correct string and "False" for the incorrect string. You need to only return a string that performs a minimum number of multiplications.

#User function Template for python3

class Solution:
    def matrixChainOrder(self, p, n):
        # code here
        infinite = float('inf')
        cost = [[infinite for _ in range(n)] for _ in range(n)]
        bracket = [['' for _ in range(n)] for _ in range(n)]

        for i in range(n - 1):
            cost[i][i + 1] = 0
            bracket[i][i + 1] = chr(ord('A') + i)

        for i in range(2, n):
            for j in range(n - i):
                x = i + j
                for k in range(j + 1, n):
                    if cost[j][x] > cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]:
                        cost[j][x] = cost[j][k] + cost[k][x] + p[j] * p[x] * p[k]
                        bracket[j][x] = '(' + bracket[j][k] + bracket[k][x] + ')'

        return bracket[0][n - 1]
