# Last Updated: 2/5/2026, 9:26:14 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            slow,fast=slow.next,fast.next
        slow.next=slow.next.next
        return head