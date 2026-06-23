# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        curr = head
        gap = ListNode()
        gap.next = head

        if not head.next:
            return None

        while curr.next:

            if count < n:
                count+=1
            else:
                gap = gap.next

            curr = curr.next
        
 
        if gap.next == head:
            return head.next
        else:
            gap.next = gap.next.next
            return head
        