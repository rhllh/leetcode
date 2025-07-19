"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    # recursion
    
    if not head:
        return
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead
        
    