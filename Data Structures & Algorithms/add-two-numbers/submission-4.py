# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The digits are aligned as we traverse both linked lists:
        
        carry?

        "1 -> 2 -> 3"
        "4 -> 5 -> 9"
        
        3 + 9 = 12 % 10 
        carry = 12 // 10
        5 -> 7 -> 2 -> 1

        """

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            
            total = val1 + val2 + carry

            new = ListNode(total % 10)
            carry = total // 10

            curr.next = new
            curr = new

        return dummy.next
            