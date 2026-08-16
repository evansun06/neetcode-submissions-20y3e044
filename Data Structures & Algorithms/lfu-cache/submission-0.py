class DLL_Node:

    def __init__(self, key, val, frequency):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        self.frequency = frequency


class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete(self, node):

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        # Prevent stale pointers when the node is added to another DLL.
        node.prev = None
        node.next = None

        self.size -= 1

    def add_tail(self, node):
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1


class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.keyMap: dict[int, DLL_Node] = {}
        self.freqMap: dict[int, DLL] = {}
        self.minFrequency = 0

    def _updateFrequency(self, node):
        old_frequency = node.frequency
        dll_stale = self.freqMap[old_frequency]

        # Remove the node from its current frequency lane.
        dll_stale.delete(node)

        # Remove an empty frequency lane.
        if dll_stale.size == 0:
            del self.freqMap[old_frequency]

            # The accessed node is moving from f to f + 1, so if its old
            # lane was the minimum and is now empty, the minimum becomes f + 1.
            if self.minFrequency == old_frequency:
                self.minFrequency += 1

        node.frequency += 1

        # Create the new frequency lane if necessary.
        if node.frequency not in self.freqMap:
            self.freqMap[node.frequency] = DLL()

        # This must happen even if the frequency lane already existed.
        self.freqMap[node.frequency].add_tail(node)

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]

            # Move the node into its new frequency lane.
            self._updateFrequency(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self._updateFrequency(node)

        else:
            if self.size == self.capacity:
                # Remove the least frequent, least recently used node.
                least_frequent_dll = self.freqMap[self.minFrequency]
                node_to_delete = least_frequent_dll.head

                least_frequent_dll.delete(node_to_delete)
                del self.keyMap[node_to_delete.key]

                if least_frequent_dll.size == 0:
                    del self.freqMap[self.minFrequency]

                self.size -= 1

            if 1 not in self.freqMap:
                self.freqMap[1] = DLL()

            node = DLL_Node(key, value, 1)
            self.freqMap[1].add_tail(node)

            self.minFrequency = 1
            self.keyMap[key] = node
            self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

"""
LFU Cache
    maintain:
        - map[key - Node] O(1): frequency
        - map[frequency - DLL]

DLL
    Head: least recently used Node at this frequency
    Tail: most recently used Node at this frequency

Node
    Prev: Node
    Next: Node
    Key: int
    Val: int
    Frequency: int

* Doubly linked list encodes recency within each frequency.
"""