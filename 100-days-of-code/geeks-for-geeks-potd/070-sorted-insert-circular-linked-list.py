# Sorted insert for circular linked list
# EasyAccuracy: 25.56%
# Given a sorted circular linked list of length n, the task is to insert a new node in this circular list 
# so that it remains a sorted circular linked list.

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class Solution:
    def sortedInsert(self, head, data):
        newnode=Node(data)
        if head == None:
            newnode.next=newnode
            return newnode
        temp=head
        if data < head.data:
            while temp.next != head:
                temp=temp.next
            temp.next=newnode
            newnode.next=head
            return newnode
        while temp.next != head and temp.next.data < data :
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
        return head