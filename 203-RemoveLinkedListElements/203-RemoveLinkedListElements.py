# Last Updated: 2/5/2026, 9:24:20 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        while head and head.val==val:
            head=head.next
        temp=head
        while temp and temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
        