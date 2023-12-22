# Candy

# There are N children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:

# Each child must have atleast one candy.
# Children with a higher rating than its neighbors get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute.

class Solution:
    def minCandy(self, n, ratings):
        left=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        right=1
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                right+=1
                left[j]=max(left[j],right)
            else:
                right=1
        return sum(left)