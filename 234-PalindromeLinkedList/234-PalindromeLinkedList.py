# Last Updated: 2/5/2026, 9:24:07 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        dummy=None
        while slow:
            temp=slow.next
            slow.next=dummy
            dummy=slow
            slow=temp
        h1,h2=head,dummy
        while h1 and h2:
            if h1.val!=h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True
            
