# 997. Find the Town Judge
# Solved
# Easy
# Topics
# Companies
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt1 = [0] * (n + 1)
        cnt2 = [0] * (n + 1)
        for a, b in trust:
            cnt1[a] += 1
            cnt2[b] += 1
        for i in range(1, n + 1):
            if cnt1[i] == 0 and cnt2[i] == n - 1:
                return i
        return -1