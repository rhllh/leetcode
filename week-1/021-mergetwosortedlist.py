"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()              # dummy node for merged list
        cursor = dummy                  # pointer for traversing node

        while list1 and list2:          # we've not reached the end of either list
            if list1.val < list2.val:   
                cursor.next = list1     # point to smaller of the current two nodes
                list1 = list1.next      # move that list's pointer forward
            else:
                cursor.next = list2
                list2 = list2.next
            
            cursor = cursor.next        # move the dummy's pointer forward
        
        if list1:                       # point to any remaining node that is not None
            cursor.next = list1
        else:
            cursor.next = list2

        return dummy.next               # return head of merged list
    
    
"""
# recursion 
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # base case, end recursion if either is empty and return the remaining list
    if not list1 or not list2:
        return list1 if list1 else list2
        
    if list1.val > list2.val:               # we are making list1 the merged list so its node will be the smaller one
        list1, list2 = list2, list1
        
    list1.next = self.mergeTwoLists(list1.next, list2)      # move list1 pointer forward, then compare the two nodes again
    return list1
"""