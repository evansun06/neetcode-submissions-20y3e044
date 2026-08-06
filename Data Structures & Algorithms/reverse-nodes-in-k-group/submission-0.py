# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        result = dummy
        curr = head
        
        while curr:

            i = 0
            
            temp = curr

            while i < k:
                if temp is None:
                    break
                else:
                    i += 1
                    temp = temp.next
            
            if i != k:
                result.next = curr
                break
            else:
                i = 0
                rev = None
                temp = None
                temp2 = curr
                while i < k:
                    temp = curr.next
                    curr.next = rev
                    rev = curr
                    curr = temp
                    i += 1


                result.next = rev
                result = temp2

        return dummy.next