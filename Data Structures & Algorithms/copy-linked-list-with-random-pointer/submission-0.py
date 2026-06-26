"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first pass
        # second pass copy all nodes and values except `random`
        # hashmap {og_pointer: index}
        # array:Node []
        # hashmap {og}

        dummy = Node(0, None, None)
        prev = dummy
        order_map = {}
        curr = head

        i = 0
        arr = []
        while curr:
            n = Node(curr.val, None, None )
            arr.append(n)
            prev.next = n
            prev = n
            order_map[curr] = i
            i += 1
            curr = curr.next
        
        copy_curr = dummy.next
        og_curr = head
        while copy_curr:
            if og_curr.random is None:
                copy_curr.random = None
            else:
                i = order_map[og_curr.random]
                copy_curr.random = arr[i]

            copy_curr = copy_curr.next
            og_curr = og_curr.next

        return dummy.next
            