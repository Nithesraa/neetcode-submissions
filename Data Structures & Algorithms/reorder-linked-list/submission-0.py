# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow , fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        f = head
        r = prev
        slow.next = None
        while r :
            tmp1 = f.next
            tmp2 = r.next
            f.next = r
            r.next = tmp1
            f = tmp1
            r = tmp2
        
