# Vertex Cover
# HardAccuracy: 62.97%


# Vertex cover of an undirected graph is a list of vertices such that every vertex not in 
# the vertex cover shares their every edge with the vertices in the vertex cover. In other words, 
# for every edge in the graph, atleast one of the endpoints of the graph should belong to the vertex cover. 
# You will be given an undirected graph G, 
# and your task is to determine the smallest possible size of a vertex cover.


from typing import List


class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        from collections import defaultdict
        from itertools import combinations
        ve=defaultdict(set)
        for i,v in enumerate(edges):
            sta,sto=v
            ve[sta-1].add(i)
            ve[sto-1].add(i)
        numedges=len(edges)
        def ok(lim):
            nonlocal ve,numedges,n
            for comb in combinations([*range(n)],lim):
                seen=set()
                for ele in comb:
                    for i in ve[ele]:
                        seen.add(i)
                        if len(seen)==numedges:
                            return True
            return False
        l=0
        r=n+1
        while l<r:
            m=l+(r-l)//2
            if ok(m):
                r=m
            else:
                l=m+1
        return l

        