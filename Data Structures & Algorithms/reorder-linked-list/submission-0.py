# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # brute force O(3n)
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        half = count // 2
        
        curr = head
        while curr and half > 0:
            curr = curr.next
            half -= 1
        
        temp = curr.next
        curr.next = None
        curr = temp
        
        rev = None
        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        
        first = head
        while rev:
            temp1 = first.next
            temp2 = rev.next
            first.next = rev
            rev.next = temp1

            first = temp1
            rev = temp2
            



            
        