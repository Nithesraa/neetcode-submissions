# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        group = 0
        while dummy and group < k:
            group+=1
            dummy = dummy.next
        if group == k:
            dummy = self.reverseKGroup(dummy,k)
            while group > 0:
                tmp = head.next
                head.next = dummy 
                dummy = head
                head = tmp
                group -=1
            head = dummy
        return head