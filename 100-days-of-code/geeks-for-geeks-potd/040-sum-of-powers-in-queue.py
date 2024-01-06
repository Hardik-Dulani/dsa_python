# Techfest and the Queue

# A Techfest is underway, and each participant is given a ticket with a unique number. 
# Organizers decide to award prize points to everyone who has a ticket ID between a and b (inclusive). 
# The points given to a participant with ticket number x will be the sum of powers of the prime factors of x.

# For instance, if points are to be awarded to a participant with ticket number 12, 
# the amount of points given out will be equal to the sum of powers in the prime factorization of 12 (22 × 31), which will be 2 + 1 = 3.

# Given a and b, determine the sum of all the points that will be awarded to the participants with ticket numbers between a and b (inclusive).


from typing import List
import math
from collections import defaultdict
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        def sieve():
            for i in range(2, maxn,2) :
                spf[i] = 2 
            for i in range(3, math.ceil(math.sqrt(maxn))):
                if spf[i] == i:
                    for j in range(i, maxn, i):
                        spf[j] = i
        maxn = b+1
        spf = [i for i in range(maxn+1)]
        hmap = defaultdict(int)
        sieve()
        def prime_factorization(num):
            while(num != 1):
                hmap[spf[num]] += 1
                num = num//spf[num]
        # print(spf)
        for i in range(a, b+1):
            prime_factorization(i)
        # print(hmap)
        return sum(hmap.values())
        

