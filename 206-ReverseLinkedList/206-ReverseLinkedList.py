# Last Updated: 2/5/2026, 9:24:17 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pn=None
        cn=head
        nn=head.next
        while cn:
            cn.next=pn
            pn=cn
            cn=nn
            if nn:
                nn=nn.next
        return pn