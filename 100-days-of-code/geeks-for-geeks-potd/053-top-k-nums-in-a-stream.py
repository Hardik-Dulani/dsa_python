# #User function Template for python3
# Top k numbers in a stream
# MediumAccuracy: 49.1%
# Given N numbers in an array, your task is to keep at most the top K numbers with respect to their frequency.

# In other words, you have to iterate over the array, and after each index, 
# determine the top K most frequent numbers until that iteration and store them in an array in decreasing order of frequency. 
# An array will be formed for each iteration and stored in an array of arrays. If the total number of distinct elements is less than K, 
# then keep all the distinct numbers in the array. If two numbers have equal frequency, 
# place the smaller number first in the array.



class Solution:
    def kTop(self,a, N, K):
        #code here.
        '''
        ans = []
        freq = {}
        for i in range(N):
            if a[i] == 0:
                continue

            if a[i] in freq:
                freq[a[i]] += 1
            else:
                freq[a[i]] = 1

            d = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
            temp = [x[0] for x in d]
            ans.append(temp[:K])

        return ans
        '''
        '''
        ans = []
        for i in range(N):
            if a[i] == 0:
                continue
            d = {}
            curr = a[:i+1]
            for j in curr:
                d[j] = d.get(j,0) + 1
            d = sorted(d.items(), key=lambda x:(-x[1],x[0]))
            temp = [x[0] for x in d]
            ans.append(temp[:k])
        return ans
        '''
        final_ans=[]
        top = [0 for i in range(K + 1)] 
        freq = {i:0 for i in range(K + 1)} 
      
        for m in range(N): 
            if a[m] in freq.keys(): 
                freq[a[m]] += 1
            else: 
                freq[a[m]] = 1
      
            top[k] = a[m] 
            i = top.index(a[m]) 
            i -= 1
              
            while i >= 0: 
                if (freq[top[i]] < freq[top[i + 1]]): 
                    t = top[i] 
                    top[i] = top[i + 1] 
                    top[i + 1] = t 
                   
                elif ((freq[top[i]] == freq[top[i + 1]]) and (top[i] > top[i + 1])): 
                    t = top[i] 
                    top[i] = top[i + 1] 
                    top[i + 1] = t 
                else: 
                    break
                i -= 1
              
            i = 0
            ans = []
            while i < K and top[i] != 0: 
                ans.append(top[i]) 
                i += 1
            
            final_ans += [ans]
        return final_ans
