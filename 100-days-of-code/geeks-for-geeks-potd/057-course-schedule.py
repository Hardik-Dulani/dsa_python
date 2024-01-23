# Course Schedule
# MediumAccuracy: 51.77%
# There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisite tasks, 
# for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
# Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you should pick to finish all tasks.
# Note: There may be multiple correct orders, you just need to return any one of them. 
# If it is impossible to finish all tasks, return an empty array. Driver code will print "No Ordering Possible",
#  on returning an empty array. Returning any correct order will give the output as 1, whereas any invalid order will give the output 0. 

#User function Template for python3

class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        from collections import defaultdict
        g = defaultdict(list)
        degree = [0]*n
        for to, frm in prerequisites:
            g[frm].append(to)
            degree[to] += 1
        
        q = [i for i, e in enumerate(degree) if e == 0]

        orders = []
        while q:
            node = q.pop()
            orders.append(node)
            for nbr in g[node]:
                degree[nbr] -= 1
                if degree[nbr] == 0:
                    q.append(nbr)
        return orders if len(orders) == n else []
