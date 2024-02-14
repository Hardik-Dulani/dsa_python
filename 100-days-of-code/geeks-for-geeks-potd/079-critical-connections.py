# Find all Critical Connections in the Graph
# HardAccuracy: 50.25%
# A critical connection refers to an edge that, upon removal, will make it impossible for certain nodes to reach each other through any path. You are given an undirected connected graph with v vertices and e edges and each vertex distinct and ranges from 0 to v-1, and you have to find all critical connections in the graph. It is ensured that there is at least one such edge present.

# Note: The answers may be presented in various potential orders. Each edge should be displayed in sorted order. For instance, if there's an edge between node 1 and node 2, it should be stored as (1,2) rather than (2,1). Additionally, it is expected that you store the edges in sorted order.


class Solution:
    def criticalConnections(self, v, adj):
        # code here
        def dfs(u, parent, disc, low, bridges):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            for v in adj[u]:
                if disc[v] == -1:  # v is not visited
                    dfs(v, u, disc, low, bridges)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((min(u, v), max(u, v)))
                elif v != parent:  # v is visited and not parent
                    low[u] = min(low[u], disc[v])

        disc = [-1] * v
        low = [-1] * v
        time = 0
        bridges = []
        for i in range(v):
            if disc[i] == -1:
                dfs(i, -1, disc, low, bridges)
        return sorted(bridges)