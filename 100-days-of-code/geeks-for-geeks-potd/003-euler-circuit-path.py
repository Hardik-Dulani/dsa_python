# An Eulerian Path is a path in graph that visits every edge exactly once
# and it starts and ends up at different indexes. 
# An Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.
# Given an undirected acyclic graph with V nodes, and E edges, with adjacency list adj, 
# return 2 if the graph contains an eulerian circuit,
# else if the graph contains an eulerian path, return 1, otherwise, return 0.
class Solution:
    def isEulerCircuitExist(self, V, adj):
        c=0
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                c+=1
        if c==0:
            return 2
        if c==2:
            return 1
        return 0