# Clone an Undirected Graph
# MediumAccuracy: 67.49%
# Given a connected undirected graph with n nodes and m edges, with each node having a distinct label from 0 to n-1, 
# create a clone of the graph. Each node in the graph contains an integer val and an array (neighbors) of nodes, containing nodes that are adjacent to the current node.

# Note: If the user returns a correct copy of the given graph, then the system will print 1; in the case when an incorrect copy is generated or when the user returns the original node, the system will print 0.

#User function Template for python3
from sys import setrecursionlimit
'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        setrecursionlimit(10**4)
        corr = dict()
        q = [node]
        while q:
            cur = q.pop()
            corr[cur] = Node()
            for nxt in cur.neighbors:
                if nxt not in corr:
                    q.append(nxt)
                    
        for ex, ne in corr.items():
            ne.val = ex.val
            ne.neighbors = [corr[x] for x in ex.neighbors]
            
        return corr[node]
        #your code goes here

