# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        head of each linked list, is the least significant digit of each number.

        iterate through both linked lists while at least one head is not null or carry is not null
        - add sum = l1.val and l2.val + carry
        - create a new node = sum / 10 
        - if sum > 9:
            - carry = sum % 10
        """

        dummy = ListNode()
        curr = dummy

        carry = 0
        while(l1 or l2 or carry != 0):
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next
            if l2 is not None:
                total += l2.val
                l2 = l2.next

            curr.next = ListNode(total % 10)
            curr = curr.next
            carry = total // 10

        return dummy.next