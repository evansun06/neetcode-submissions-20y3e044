# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0, head)
        trail =  dummy

        while n > 0:
            n -= 1
            curr = curr.next
        
        while curr:
            curr = curr.next
            trail = trail.next
        
        trail.next = trail.next.next

        return dummy.next

            
    