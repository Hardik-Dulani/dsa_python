# Largest rectangular sub-matrix whose sum is 0

# Given a matrix mat[][] of size N x M. The task is to find the largest rectangular sub-matrix by area whose sum is 0.

# If there are multiple solutions return the rectangle which starts from minimum column index. 
# If you still have multiple solutions return the one having greatest row number. If no such matrix is present return a zero (0) size matrix.

from typing import List

class Solution:
    def sumZeroMatrix(self,a: List[List[int]]) -> List[List[int]]:
        m=len(a)
        n=len(a[0])
        left,right,up,down=0,0,0,0
        for i in range(n):
            arr=[0]*m
            for j in range(i,n):
                for k in range(m):
                    arr[k]+=a[k][j]
                sum_map={0: -1}
                l,r=0,0
                curr_sum=0
                for k in range(m):
                    curr_sum+=arr[k]
                    if curr_sum in sum_map:
                        if k-sum_map[curr_sum]>r-l:
                            l=sum_map[curr_sum]+1
                            r=k+1
                    else:
                        sum_map[curr_sum]=k
                if (j-i+1)*(r-l)>(right-left)*(down-up):
                    up=l
                    down=r
                    left=i
                    right=j+1

        result=[]
        for i in range(up,down):
            row=[]
            for j in range(left,right):
                row.append(a[i][j])
            result.append(row)

        return result

