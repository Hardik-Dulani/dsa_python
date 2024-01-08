# Merge 2 sorted linked list in reverse order
# MediumAccuracy: 62.29%
# Given two linked lists of size N and M, which are sorted in non-decreasing order. 
# The task is to merge them in such a way that the resulting list is in non-increasing order

#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
       
            result=None
            
            #Iterate through both linked lists
            while h1 and h2:
                
                #If the data in h1 is less than or equal to the data in h2,
                #set h1.next as the result, update result to h1, and move h1 to the next node.
                if h1.data<=h2.data:
                    temp=h1.next
                    h1.next=result
                    result=h1
                    h1=temp
                
                #If the data in h2 is less than the data in h1,
                #set h2.next as the result, update result to h2, and move h2 to the next node.
                else:
                    temp=h2.next
                    h2.next=result
                    result=h2
                    h2=temp
            
            #If there are remaining nodes in h1, append them to the result list.
            while h1:
                temp=h1.next
                h1.next=result
                result=h1
                h1=temp
                
            #If there are remaining nodes in h2, append them to the result list.
            while h2:
                temp=h2.next
                h2.next=result
                result=h2
                h2=temp
            
            #Return the final merged linked list.
            return result

    
       
            