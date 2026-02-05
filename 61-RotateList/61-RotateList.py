# Last Updated: 2/5/2026, 9:25:40 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        while k==0 or head is None or head.next is None:
            return head
        l=0
        cn=head
        while cn!=None:
            cn=cn.next
            l+=1
        k=k%l
        if k==0:
            return head
        step=l-k-1
        cn=head
        while step:
            cn=cn.next
            step-=1
        nhead=cn.next
        cn.next=None
        cn=nhead
        while cn.next:
            cn=cn.next
        cn.next=head
        return nhead
        