# Given a directed graph with V nodes and E edges, if there is an edge from u to v, 
# then we will say that u depends on v. 
# Number of Dependencies (NoD) for a node x is the total count of nodes that x depends upon.
# Find out the sum of number of dependencies of every node.

class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        sum=0
        for i in adj:
            sum+=len(i)
        return sum
