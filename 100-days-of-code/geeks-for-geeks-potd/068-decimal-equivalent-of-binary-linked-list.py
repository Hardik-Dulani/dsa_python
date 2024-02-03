# Decimal Equivalent of Binary Linked List
# EasyAccuracy: 21.23%
# Given a singly linked list of length n. The link list represents a binary number, 
# ie- it contains only 0s and 1s. Find its decimal equivalent.
# The significance of the bits decreases with the increasing index in the linked list.
# An empty linked list is considered to represent the decimal value 0. 

# Since the answer can be very large, answer modulo 109+7 should be printed.

# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        # Code here
        p=None
        c=head
        while c:
            n=c.next
            c.next=p
            p,c=c,n
        nh=p
        ans=0
        power=0
        while nh is not None:
            ans+=nh.data*(2**power)
            ans=ans%MOD
            power+=1
            nh=nh.next
        return ans
