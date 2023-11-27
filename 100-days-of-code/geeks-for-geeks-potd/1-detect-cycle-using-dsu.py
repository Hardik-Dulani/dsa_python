class Solution:

    #Function to detect cycle using DSU in an undirected graph.
    def find(self, n, parent):
        if parent[n] == n:
            return n
        parent[n] = self.find(parent[n], parent)
        return parent[n]

    def union(self, a, b, parent):
        x = self.find(a, parent)
        y = self.find(b, parent)
        if x != y:
            parent[x] = y
            return False
        return True
        
    #Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        #Code here
        parent = list(range(V))

        for i in range(V):
            for j in range(len(adj[i])):
                if i < adj[i][j] and self.union(i, adj[i][j], parent):
                    return 1
        return 0
