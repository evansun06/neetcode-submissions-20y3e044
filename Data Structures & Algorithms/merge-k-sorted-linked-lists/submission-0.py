# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy

        while True:
            min_node = None
            min_index = 0
            for i, node in enumerate(lists):

                if node is None:
                    continue

                if min_node is None or node.val < min_node.val:
                    min_node = node
                    min_index = i
                
                
            if min_node == None:
                break
            else:
                lists[min_index] = min_node.next
            
            min_node.next = None
            curr.next = min_node
            curr = curr.next
        
        return dummy.next


                






        