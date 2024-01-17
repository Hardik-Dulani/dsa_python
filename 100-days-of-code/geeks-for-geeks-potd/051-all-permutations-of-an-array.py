# All Unique Permutations of an array
# MediumAccuracy: 52.85%

# Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. 
# A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.


#User function Template for python3

class Solution:
    def permutations(self,h,arr,index):
        # code here 
        if index==len(arr):
            h.add(tuple(arr))
            return
        for i in range(index,len(arr)):
            arr[index],arr[i]=arr[i],arr[index]
            self.permutations(h,arr,index+1)
            arr[index],arr[i]=arr[i],arr[index]
    def uniquePerms(self, arr, n):
        # code here 
        h,ans=set(),[]
        self.permutations(h,arr,0)
        for i in h: ans.append(i)
        ans.sort()
        return ans
