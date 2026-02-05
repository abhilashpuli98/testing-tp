# Last Updated: 2/5/2026, 9:26:11 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        dummy=ListNode()
        newhead=dummy
        while h1 and h2:
            if h1.val<=h2.val:
                newhead.next=h1
                h1=h1.next
            else:
                newhead.next=h2
                h2=h2.next
            newhead=newhead.next
        if h1:
            newhead.next=h1
        if h2:
            newhead.next=h2

        return dummy.next