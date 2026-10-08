class LRUCache:
    """
    Maintain some datastructure that efficiently allows removals
    and can track recency

    queue implemented with a doubly linked list

    - head pointer: the least recently used node
    - tail pointer: the most recently used node and enqueue location

    map {key : DLL}
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]

            self.delete(node)
            # make node most recent
            self.addToTail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.delete(node)
            self.addToTail(node)
            return

        if len(self.node_map) == self.capacity:
            oldest = self.head
            self.delete(oldest)
            del self.node_map[oldest.key]
        
        node = DLLNode(value, key)
        self.node_map[key] = node
        self.addToTail(node)

    def delete(self, node):
        if self.head is node:
            self.head = node.nxt
        if self.tail is node:
            self.tail = node.prev
        
        if node.nxt:
            node.nxt.prev = node.prev
        if node.prev:
            node.prev.nxt = node.nxt
        
        node.prev = None
        node.nxt = None

    def addToTail(self, node):
        node.prev = self.tail
        node.nxt = None

        if self.tail:
            self.tail.nxt = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        

class DLLNode:

    def __init__(self, val, key, nxt = None, prev = None):
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev