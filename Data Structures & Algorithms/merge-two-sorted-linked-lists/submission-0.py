# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        merged = dummy
    
        while curr1 or curr2:
            if curr1 is None:
                merged.next = curr2
                break
            elif curr2 is None:
                merged.next = curr1
                break
            elif curr1.val <= curr2.val:
                merged.next = curr1
                merged = curr1
                curr1 = curr1.next
            else:
                merged.next = curr2
                merged = curr2
                curr2 = curr2.next
        
        return dummy.next
            
