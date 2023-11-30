# Consider a directed graph whose vertices are numbered from 1 to n.
# There is an edge from a vertex i to a vertex j if and only if either j = i + 1 or j = 3 * i.
# The task is to find the minimum number of edges in a path from vertex 1 to vertex n.
class Solution:
    def minimumStep (self, n):
        ans = 0
        
        while n >= 3:
            ans += n % 3 + 1
            n //= 3
        
        return ans + (n - 1)
        