# Maximum Meetings in One Room

# There is one meeting room in a firm. 
# There are N meetings in the form of (S[i], F[i]) 
# where S[i] is the start time of meeting i and F[i] is the finish time of meeting i. 
# The task is to find the maximum number of meetings that can be accommodated in the meeting room.
# You can accommodate a meeting if the start time of the meeting is strictly greater than the finish time of the previous meeting. 
# Print all meeting numbers.

# Note: If two meetings can be chosen for the same slot then choose meeting with smaller index in the given array.

from typing import List

class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        l = []
        for i in range(N):
            l.append([S[i],F[i],i+1])
            
        #Sorting the list according to end time(F[i]) of meeting
        l.sort(key = lambda x: x[1])
        
        ans = [l[0][2]]
        end = l[0][1]
        for i in range(1,len(l)):
            if l[i][0]>end:
                ans.append(l[i][2])
                end = l[i][1]
            
        ans.sort()
        return ans
