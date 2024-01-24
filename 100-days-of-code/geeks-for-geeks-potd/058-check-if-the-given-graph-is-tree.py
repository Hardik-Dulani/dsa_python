# Check if a given graph is tree or not
# MediumAccuracy: 54.18%
# You are given an undirected graph of N nodes and M edges. Return 1 if the graph is a tree, else return 0.

# Note: The input graph can have self-loops and multiple edges.



from collections import defaultdict

class Solution:
    def isTree(self, n, m, edges):
        def helper(u, par, vis, g):
            vis[u] = 1
            flag = True
            for c in g[u]:
                if c == par:
                    continue
                if vis[c]:
                    return False
                flag = flag and helper(c, u, vis, g)
            return flag

        g = defaultdict(list)
        for i in range(m):
            g[edges[i][0]].append(edges[i][1])
            g[edges[i][1]].append(edges[i][0])

        vis = [0] * n
        ans = helper(0, -1, vis, g)

        for v in vis:
            if v == 0:
                ans = False
                break

        return int(ans)
