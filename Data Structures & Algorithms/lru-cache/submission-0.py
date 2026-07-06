class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_map = {}
        self.head: DLLNode = None  # most recent
        self.tail: DLLNode = None  # least recent

    def _add_to_head(self, node):
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1

        curr = self.value_map[key]

        self._remove(curr)
        self._add_to_head(curr)

        return curr.value

    def put(self, key: int, value: int) -> None:
        if key in self.value_map:
            curr = self.value_map[key]
            curr.value = value

            self._remove(curr)
            self._add_to_head(curr)

        else:
            new = DLLNode(key, value, None, None)
            self.value_map[key] = new
            self._add_to_head(new)

            if len(self.value_map) > self.capacity:
                lru = self.tail
                self._remove(lru)
                del self.value_map[lru.key]


class DLLNode:
    def __init__(self, key: int, value: int, prev: "DLLNode", next: "DLLNode"):
        self.key = key
        self.value = value
        self.prev = prev if prev else None
        self.next = next if next else None