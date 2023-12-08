# Transform to prime


# Given an array of n integers. 
# Find the minimum non-negative number to be inserted in array, so that sum of all elements of array becomes prime
class Solution:
    def minNumber(self, arr,n):
        sum_arr = sum(arr)
        if sum_arr==1:
            return 1
        if sum_arr == 0:
            return 2  
        def isPrime(number):
            if number<2:
                return False
            if number==2:
                return True
                
                
            for i in range(2,int(number**(0.5))+1): 
                if not number%i:
                    return False
            return True
        i = 0
        while not isPrime(sum_arr):
            sum_arr+=1
            i+=1
        return i
        